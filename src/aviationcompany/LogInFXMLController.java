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
import javafx.fxml.Initializable;
import javafx.scene.Node;
import javafx.scene.Parent;
import javafx.scene.Scene;
import javafx.scene.control.Button;
import javafx.scene.control.Label;
import javafx.scene.control.PasswordField;
import javafx.scene.control.TextField;
import javafx.scene.layout.AnchorPane;
import javafx.stage.Stage;

/**
 *
 * @author Tanbin
 */
public class LogInFXMLController implements Initializable {

    @FXML
    private ResourceBundle resources;
    @FXML
    private AnchorPane logInPane;

    @FXML
    private URL location;

    @FXML
    private TextField userID;

    @FXML
    private PasswordField pass;

    @FXML
    private Button login;

    @FXML
    private Button register;

    @FXML

    void handleLogInBtn(ActionEvent event) throws IOException {
        
        if ("admin".equals(userID.getText())) {
            Parent admin = FXMLLoader.load(getClass().getResource("/Admin/AdminFXML.fxml"));
            Scene adminScene = new Scene(admin);
            Stage window = (Stage) ((Node) event.getSource()).getScene().getWindow();
            window.setScene(adminScene);
            window.setTitle("Aviation Admin");
            window.show();
        }
        else if("management".equals(userID.getText())){
            Parent admin = FXMLLoader.load(getClass().getResource(""));
            Scene adminScene = new Scene(admin);
            Stage window = (Stage) ((Node) event.getSource()).getScene().getWindow();
            window.setScene(adminScene);
            window.setTitle("Aviation Managment");
            window.show();
            
        } 
        else if("client".equals(userID.getText())){
            Parent admin = FXMLLoader.load(getClass().getResource("/Client/ClientFXML.fxml"));
            Scene adminScene = new Scene(admin);
            Stage window = (Stage) ((Node) event.getSource()).getScene().getWindow();
            window.setScene(adminScene);
            window.setTitle("Aviation  Client");
            window.show();
            
        } 
        else if("lendingCompany".equals(userID.getText())){
            Parent admin = FXMLLoader.load(getClass().getResource(""));
            Scene adminScene = new Scene(admin);
            Stage window = (Stage) ((Node) event.getSource()).getScene().getWindow();
            window.setScene(adminScene);
            window.setTitle("Aviation Client");
            window.show();
            
        } 
        else if("pilot".equals(userID.getText())){
            Parent admin = FXMLLoader.load(getClass().getResource("/Pilot/PilotFXML.fxml"));
            Scene adminScene = new Scene(admin);
            Stage window = (Stage) ((Node) event.getSource()).getScene().getWindow();
            window.setScene(adminScene);
            window.setTitle("Aviation Pilot");
            window.show();
            
        } 

//        MD5 md5=new MD5();
//        System.out.println(md5.getMd5(pass.getText()));
    }

    @FXML

    void handleRegBtn(ActionEvent event) throws IOException {
        Parent reg = FXMLLoader.load(getClass().getResource("RegisterFXML.fxml"));
        Scene regScene = new Scene(reg);
        Stage window = (Stage) ((Node) event.getSource()).getScene().getWindow();
        window.setScene(regScene);
        window.setTitle("Client Registration");
        window.show();

//        AnchorPane regPane = FXMLLoader.load(getClass().getResource("RegisterFXML.fxml"));
//        logInPane.getChildren().setAll(regPane);
    }

    @Override
    public void initialize(URL url, ResourceBundle rb) {
        // TODO
    }

}
