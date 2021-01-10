/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package BookingManagement;

import java.io.IOException;
import java.net.URL;
import java.util.ResourceBundle;
import javafx.event.ActionEvent;
import javafx.fxml.FXML;
import javafx.fxml.FXMLLoader;
import javafx.fxml.Initializable;
import javafx.scene.Parent;
import javafx.scene.Scene;
import javafx.scene.control.Button;
import javafx.scene.control.Menu;
import javafx.scene.control.MenuItem;
import javafx.scene.control.ScrollPane;
import javafx.stage.Stage;

/**
 * FXML Controller class
 *
 * @author ronok
 */
public class BookingManagementFXMLController implements Initializable {

    @FXML
    private Menu home;
    @FXML
    private MenuItem goHome;
    @FXML
    private MenuItem logOut;
    @FXML
    private MenuItem about;
    @FXML
    private Button fightScd;
    @FXML
    private Button assignPilot;
    @FXML
    private Button viewClientChange;
    @FXML
    private Button feedback;
    @FXML
    private ScrollPane body;
    @FXML
    private Button viewPilotChange;

    /**
     * Initializes the controller class.
     */
    @Override
    public void initialize(URL url, ResourceBundle rb) {
        // TODO
    }    

    @FXML
    private void goHomeAction(ActionEvent event) {
    }

    @FXML
    private void logOut(ActionEvent event) throws IOException {
            Parent logIn = FXMLLoader.load(getClass().getResource("/aviationcompany/LogInFXML.fxml"));
        Scene logInScene = new Scene(logIn);
        Stage window = (Stage) body.getScene().getWindow();
        window.setScene(logInScene);
        window.setTitle("Aviation LogIn");
        window.show();
    }

    @FXML
    private void aboutAction(ActionEvent event) {
    }

    @FXML
    private void flightScdA(ActionEvent event) {
        System.out.println("ClickedMe");
    }



    @FXML
    private void viewClientChangeA(ActionEvent event) {
    }

    @FXML
    private void feedbackA(ActionEvent event) {
    }

    @FXML
    private void assignPilotAction(ActionEvent event) {
    }

    @FXML
    private void viewPilotChangeAc(ActionEvent event) {
    }
    
}
