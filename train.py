import expression_recognition
from train_options import ToolOptions
import matplotlib.pyplot as plt


def loss_graph(train_losses,validation_losses):
    plt.plot(train_losses, 'g', label='Training loss')
    plt.plot(validation_losses, 'b', label='validation loss')
    plt.title('Training and Validation loss')
    plt.xlabel('Epochs')
    plt.ylabel('Loss')
    plt.legend()
    plt.show()

def accu_graph(train_accuracies,validation_accuracies):
    plt.plot(train_accuracies, 'g', label='Training accuracy')
    plt.plot(validation_accuracies, 'b', label='validation accuracy')
    plt.title('Training and Validation accuracy')
    plt.xlabel('Epochs')
    plt.ylabel('Accuracy')
    plt.legend()
    plt.show()
    
if __name__ == '__main__':
    opt = ToolOptions().parse()

    model = expression_recognition.ExpRecognition()
    model.prepare_devices(opt.gpu_ids, opt.landmark_num, opt.image_width)
    
    if opt.mode == 'train':
        model.load_train_data(opt.train_image_path, opt.train_label_path, opt.batch_size, opt.num_workers)
        model.load_validation_data(opt.validation_image_path, opt.validation_label_path, opt.num_workers)
        model.load_test_data(opt.test_image_path, opt.num_workers)
        model.prepare_tool(opt.start_lr, opt.learning_rate_decay_start, opt.total_epoch, opt.model_path, \
            opt.beta, opt.margin_1, opt.margin_2, opt.relabel_epoch)

        model.validation(opt.validation_path, 0)
        model.test(opt.test_path, 0)
        train_losses = []
        validation_losses = []
        train_accuracies = []
        validation_accuracies = []
        for epoch in range(1, opt.total_epoch+1):
            running_loss , running_accu = model.train(epoch)
            
            
            train_losses.append(running_loss)
            train_accuracies.append(running_accu)
            #print('test1 ' + str(train_losses))
            #print('test2 ' + str(train_accuracies))
            if epoch % opt.validation_frequency == 0:
                running_val_loss , running_val_accu = model.validation(opt.validation_path, epoch)
                validation_losses.append(running_val_loss)
                validation_accuracies.append(running_val_accu)
                #print('test3 ' + str(validation_losses))
                #print('test4 ' + str(validation_accuracies))
            if epoch % opt.save_frequency == 0:
                model.save_model(epoch, opt.save_path)
                
        
        loss_graph(train_losses,validation_losses)
        accu_graph(train_accuracies,validation_accuracies)
        model.test(opt.test_path, epoch)