
package Admin;

import java.io.IOException;
import java.net.URL;
import java.util.ResourceBundle;
import java.util.logging.Level;
import java.util.logging.Logger;
import javafx.event.ActionEvent;
import javafx.fxml.FXML;
import javafx.fxml.FXMLLoader;
import javafx.fxml.Initializable;
import javafx.scene.Node;
import javafx.scene.Parent;
import javafx.scene.Scene;
import javafx.scene.control.Button;
import javafx.scene.control.Menu;
import javafx.scene.control.MenuItem;
import javafx.scene.control.ScrollPane;
import javafx.scene.layout.AnchorPane;
import javafx.stage.Stage;

/**
 * FXML Controller class
 *
 * @author Tanbin
 */
public class AdminFXMLController implements Initializable {

    @FXML
    private Menu home;

    @FXML
    private MenuItem goHome;

    @FXML
    private MenuItem logOut;

    @FXML
    private Menu Accounts;

    @FXML
    private MenuItem createAc;

    @FXML
    private MenuItem myAc;
    @FXML
    private MenuItem about;

    @FXML
    private ScrollPane body;
    @FXML
    private Button FlightScd;
    @FXML
    private Button allFlightScd1;
    @FXML
    private Button allFlightScd2;
    @FXML
    private Button allFlightScd3;
    @FXML
    private Button allFlightScd4;

    @FXML
    void createAcAction(ActionEvent event) throws IOException {
        AnchorPane logInPane = FXMLLoader.load(getClass().getResource("CreateAcFXML.fxml"));
        body.setContent(logInPane);

    }

    @FXML
    void goHomeAction(ActionEvent event) throws IOException {
        AnchorPane pane = FXMLLoader.load(getClass().getResource("AdminHomeFXML.fxml"));
        body.setContent(pane);

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
    void myAcAction(ActionEvent event) throws IOException {
         AnchorPane pane = FXMLLoader.load(getClass().getResource("MyAcAdminFXML.fxml"));
        body.setContent(pane);

    }
    @FXML
    void aboutAction(ActionEvent event) throws IOException {
        AnchorPane pane = FXMLLoader.load(getClass().getResource("/aviationcompany/AboutFXML.fxml"));
        body.setContent(pane);
        

    }


    @Override
    public void initialize(URL url, ResourceBundle rb) {
        
        try {
            AnchorPane pane;
            pane = FXMLLoader.load(getClass().getResource("AdminHomeFXML.fxml"));
            body.setContent(pane);
        } catch (IOException ex) {
            Logger.getLogger(AdminFXMLController.class.getName()).log(Level.SEVERE, null, ex);
        }
        
    }

    @FXML
    private void FlightScdA(ActionEvent event) {
    }

    @FXML
    private void allFlightScdA(ActionEvent event) {
    }

}
