package Pilot;

import java.io.IOException;
import javafx.event.ActionEvent;
import javafx.fxml.FXML;
import javafx.fxml.FXMLLoader;
import javafx.scene.Parent;
import javafx.scene.Scene;
import javafx.scene.control.Button;
import javafx.scene.control.Menu;
import javafx.scene.control.MenuItem;
import javafx.scene.control.ScrollPane;
import javafx.scene.layout.AnchorPane;
import javafx.stage.Stage;

public class PilotFXMLController {

    @FXML
    private Menu home;

    @FXML
    private MenuItem goHome;

    @FXML
    private MenuItem logOut;

    @FXML
    private MenuItem myAc;

    @FXML
    private MenuItem about;

    @FXML
    private ScrollPane body;

    @FXML
    private Button fightScd;

    @FXML
    private Button helicopterDetail;

    @FXML
    private Button flightHis;

    @FXML
    private Button changeWorkTime;

    @FXML
    private Button feedback;

    @FXML
    void aboutAction(ActionEvent event) {

    }

    @FXML
    void changeWorkTimeA(ActionEvent event) {

    }


    @FXML
    void feedbackA(ActionEvent event) {

    }

    @FXML
    void flightHisAc(ActionEvent event) {

    }

    @FXML
    void flightScdA(ActionEvent event) throws IOException {
        AnchorPane pane = FXMLLoader.load(getClass().getResource("/aviationcompany/FlightScdFXML.fxml"));
        body.setContent(pane);

    }

    @FXML
    void goHomeAction(ActionEvent event) {

    }

    @FXML
    void helicopterDetailAction(ActionEvent event) {

    }

    @FXML
    void logOut(ActionEvent event) throws IOException {
        Parent logIn = FXMLLoader.load(getClass().getResource("/aviationcompany/LogInFXML.fxml"));
        Scene logInScene = new Scene(logIn);
        Stage window = (Stage) body.getScene().getWindow();
        window.setScene(logInScene);
        window.setTitle("Aviation LogIn");
        window.show();

    }

    @FXML
    void myAcAction(ActionEvent event) {

    }

}
