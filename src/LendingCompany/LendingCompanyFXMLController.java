package LendingCompany;

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

public class LendingCompanyFXMLController {

    @FXML
    private Menu home;

    @FXML
    private MenuItem goHome;

    @FXML
    private MenuItem logOut;

    @FXML
    private MenuItem about;

    @FXML
    private ScrollPane body;

    @FXML
    private Button addHelicopter;

    @FXML
    private Button modifyHelicopter;

    @FXML
    private Button checkBookStatus;

    @FXML
    private Button bookingConfirmation;

    @FXML
    void aboutAction(ActionEvent event) throws IOException {
        AnchorPane pane = FXMLLoader.load(getClass().getResource("/aviationcompany/AboutFXML.fxml"));
        body.setContent(pane);

    }

    @FXML
    void addHelicopterA(ActionEvent event) {

    }

    @FXML
    void bookingConfirmationA(ActionEvent event) {

    }

    @FXML
    void changeFlightSchAction(ActionEvent event) {

    }

    @FXML
    void goHomeAction(ActionEvent event) {

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
    void viewDelHelicopterAction(ActionEvent event) {

    }

}
