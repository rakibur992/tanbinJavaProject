/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package aviationcompany;

import javafx.application.Application;
import javafx.fxml.FXMLLoader;
import javafx.scene.Parent;
import javafx.scene.Scene;
import javafx.scene.image.Image;
import javafx.stage.Stage;

/**
 *
 * @author Rakib
 */
public class AviationCompany extends Application {
    
    @Override
    public void start(Stage stage) throws Exception {
        Parent root = FXMLLoader.load(getClass().getResource("LogInFXML.fxml"));
        Scene scene = new Scene(root);
        Image icon =new Image(getClass().getResourceAsStream("/img/img.jpg"));
        stage.setScene(scene);
        stage.getIcons().add(icon);
        stage.setTitle("Helicopter Aviation LogIn");
        stage.show();
    }

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        launch(args);
    }
    
}
