package Client;

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

public class ClientFXMLController {

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
    private Button fightBooking;

    @FXML
    private Button changeFlightSch;

    @FXML
    private Button checkBookStatus;

    @FXML
    private Button feedback;

    @FXML
    void aboutAction(ActionEvent event) throws IOException {
        AnchorPane pane = FXMLLoader.load(getClass().getResource("/aviationcompany/AboutFXML.fxml"));
        body.setContent(pane);

    }

    @FXML
    void changeFlightSchAction(ActionEvent event) {

    }

    @FXML
    void checkBookStatusAction(ActionEvent event) {

    }

    @FXML
    void feedbackA(ActionEvent event) {

    }

    @FXML
    void fightBookingA(ActionEvent event) {

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

}
