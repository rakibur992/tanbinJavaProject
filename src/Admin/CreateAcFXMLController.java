/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package Admin;

import MD5.MD5;
import java.io.File;
import java.io.FileWriter;
import java.io.IOException;
import java.io.PrintWriter;
import static java.lang.Thread.sleep;
import java.net.URL;
import java.util.ResourceBundle;
import java.util.concurrent.TimeUnit;
import javafx.collections.FXCollections;
import javafx.collections.ObservableList;
import javafx.event.ActionEvent;
import javafx.fxml.FXML;
import javafx.fxml.FXMLLoader;
import javafx.fxml.Initializable;
import javafx.scene.Node;
import javafx.scene.Parent;
import javafx.scene.Scene;
import javafx.scene.control.Button;
import javafx.scene.control.ChoiceBox;
import javafx.scene.control.Label;
import javafx.scene.control.TextField;
import javafx.stage.Stage;
/**
 * FXML Controller class
 *
 * @author Tanbin
 */
public class CreateAcFXMLController implements Initializable {
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
    private ChoiceBox acType;

    @FXML
    private Button register;
    
    ObservableList<String> acTypeList=FXCollections.observableArrayList("Choose Account Type","pilot","lendingCompany","management");
    @FXML
    private Label error;

    @FXML
    void registerAction(ActionEvent event) throws IOException, InterruptedException {
        File file = new File("user.txt");
        FileWriter fw= new FileWriter(file,true);
        PrintWriter pw=new PrintWriter(fw);
        MD5 md5=new MD5();
        if (pass.getText().equals(cpass.getText())) {
            String data=userName.getText()+","+userID.getText()+","+md5.getMd5(pass.getText())+","+email.getText()+","+acType.getValue();
            pw.println(data);
            pw.close();
            error.setText("Account Created"); 
        }
        else{
            error.setText("Password Mismatch");
        }

    }

    @Override
    public void initialize(URL url, ResourceBundle rb) {
        acType.setValue("Choose Account Type");
        acType.setItems(acTypeList);
        
    }    
    
}