/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package aviationcompany;

import java.net.URL;
import java.util.ResourceBundle;
import javafx.collections.FXCollections;
import javafx.collections.ObservableList;
import javafx.event.ActionEvent;
import javafx.fxml.FXML;
import javafx.fxml.Initializable;
import javafx.scene.control.Button;
import javafx.scene.control.ChoiceBox;
import javafx.scene.control.TextField;

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
    
    ObservableList<String> acTypeList=FXCollections.observableArrayList("Choose Account Type","Pilot","Helicopter Financing Company","Management");

    @FXML
    void registerAction(ActionEvent event) {

    }

    @Override
    public void initialize(URL url, ResourceBundle rb) {
        acType.setValue("Choose Account Type");
        acType.setItems(acTypeList);
        
    }    
    
}
