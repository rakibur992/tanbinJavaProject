package Admin;

import java.io.IOException;
import javafx.event.ActionEvent;
import javafx.fxml.FXML;
import javafx.fxml.FXMLLoader;
import javafx.scene.control.Button;
import javafx.scene.layout.AnchorPane;

public class AdminHomeFXMLController {

    @FXML
    private Button allFlightScd;

    @FXML
    private Button flightChangeScd;


    @FXML
    private AnchorPane homebody;
    @FXML
    private Button feedback;

    @FXML
    void allFlightScdA(ActionEvent event) throws IOException {
        AnchorPane ap = FXMLLoader.load(getClass().getResource("/aviationcompany/FlightScdFXML.fxml"));
        homebody.getChildren().setAll(ap);
    }

    @FXML
    void flightChangeScdAction(ActionEvent event) {

    }

    @FXML
    void showUserAction(ActionEvent event) {

    }

}
