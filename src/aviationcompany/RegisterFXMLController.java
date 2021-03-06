/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package aviationcompany;

import MD5.MD5;
import java.io.File;
import java.io.FileWriter;
import java.io.IOException;
import java.io.PrintWriter;
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
import javafx.scene.control.Label;
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
    private Label error;

    @FXML
    void registerAction(ActionEvent event) throws IOException {
        File file = new File("user.txt");
        FileWriter fw= new FileWriter(file,true);
        PrintWriter pw=new PrintWriter(fw);
        MD5 md5=new MD5();
        if (pass.getText().equals(cpass.getText())) {
            String data=userName.getText()+","+userID.getText()+","+md5.getMd5(pass.getText())+","+email.getText()+","+"client";
            pw.println(data);
            pw.close();
            Parent logIn = FXMLLoader.load(getClass().getResource("LogInFXML.fxml"));
            Scene logInScene = new Scene(logIn);
            Stage window = (Stage) ((Node) event.getSource()).getScene().getWindow();
            window.setScene(logInScene);
            window.setTitle("Aviation LogIn");
            window.show();
            
        }
        else{
            error.setText("Password Mismatch");
            pw.close();
        }
        

    }
    @Override
    public void initialize(URL url, ResourceBundle rb) {
        // TODO
    }    
    
}
