/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package aviationcompany;

import java.io.IOException;
import java.net.URL;
import java.util.ResourceBundle;
import javafx.event.ActionEvent;
import javafx.fxml.FXML;
import javafx.fxml.FXMLLoader;
import javafx.scene.control.Button;
import javafx.scene.control.TextField;
import javafx.fxml.Initializable;
import javafx.scene.Node;
import javafx.scene.Parent;
import javafx.scene.Scene;
import javafx.scene.layout.AnchorPane;
import javafx.stage.Stage;

/**
 * FXML Controller class
 *
 * @author Tanbin
 */
public class RegisterFXMLController implements Initializable {
    
    @FXML
    private AnchorPane regPane;

    @FXML
    private TextField userName;

    @FXML
    private TextField userID;

    @FXML
    private TextField pass;

    @FXML
    private TextField cpass;

    @FXML
    private TextField email;

    @FXML
    private Button register;

    @FXML
    void registerAction(ActionEvent event) throws IOException {
        Parent logIn = FXMLLoader.load(getClass().getResource("LogInFXML.fxml"));
        Scene logInScene = new Scene(logIn);
        Stage window = (Stage) ((Node) event.getSource()).getScene().getWindow();
        window.setScene(logInScene);
        window.setTitle("CMS LogIn");
        window.show();
//        AnchorPane logInPane = FXMLLoader.load(getClass().getResource("LogInFXML.fxml"));
//        regPane.getChildren().setAll(logInPane);

    }
    @Override
    public void initialize(URL url, ResourceBundle rb) {
        // TODO
    }    
    
}
