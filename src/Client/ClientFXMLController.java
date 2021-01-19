package Client;

import JavaClass.Booking;
import JavaClass.Client;
import JavaClass.Data;
import JavaClass.Booking;
import JavaClass.LendingCompany;
import LendingCompany.AddHelicopterFXMLController;
import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.ObjectOutputStream;
import java.net.URL;
import java.time.LocalDate;
import java.util.ResourceBundle;
import java.util.logging.Level;
import java.util.logging.Logger;
import javafx.collections.FXCollections;
import javafx.collections.ObservableList;
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
import javafx.scene.control.TableColumn;
import javafx.scene.control.TableView;
import javafx.scene.control.cell.PropertyValueFactory;
import javafx.scene.control.cell.TextFieldTableCell;
import javafx.scene.layout.AnchorPane;
import javafx.stage.Stage;

public class ClientFXMLController implements Initializable{

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
    Client cl;

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
        TableView<Booking> tableView=new TableView();
        TableColumn<Booking, String> model= new TableColumn<>("Model");
        TableColumn<Booking,String> pickUpLoc = new TableColumn<>("Pick Up Location");
        TableColumn<Booking,String> desLoc= new TableColumn<>("Destination Location");
        TableColumn<Booking,String> time= new TableColumn<>("Time");
        TableColumn<Booking, LocalDate> pickUpData= new TableColumn<>("Pick-UP Date");
        TableColumn<Booking,String> status= new TableColumn<>("Status"); 
        //set up the columns in the table
        model.setCellValueFactory(new PropertyValueFactory<>("model"));
        pickUpLoc.setCellValueFactory(new PropertyValueFactory<>("pickUpLoc"));
        desLoc.setCellValueFactory(new PropertyValueFactory<>("destinationLoc"));
        pickUpData.setCellValueFactory(new PropertyValueFactory<>("pickUpDate"));
        time.setCellValueFactory(new PropertyValueFactory<>("time"));
        status.setCellValueFactory(new PropertyValueFactory<>("status"));
        cl= (Client)Data.user;
        ObservableList<Booking> ol=FXCollections.observableArrayList(cl.getBookingList());
        tableView.setItems(ol);
        tableView.getColumns().addAll(model,pickUpLoc,desLoc,time,pickUpData,status);
//        tableView.setEditable(true);
//        model.setCellFactory(TextFieldTableCell.forTableColumn());
        body.setContent(tableView);
        

    }

    @FXML
    void feedbackA(ActionEvent event) {

    }

    @FXML
    void fightBookingA(ActionEvent event) throws IOException {
        AnchorPane pane = FXMLLoader.load(getClass().getResource("AddBookingFXML.fxml"));
        body.setContent(pane);

    }

    @FXML
    void goHomeAction(ActionEvent event) {

    }

    @FXML
    void logOut(ActionEvent event) throws IOException {
        try {
            ObjectOutputStream os=new ObjectOutputStream(new FileOutputStream(cl.getUsername()+".bin"));
            os.writeObject(Data.user);
            os.close();
        } catch (FileNotFoundException ex) {
            Logger.getLogger(AddHelicopterFXMLController.class.getName()).log(Level.SEVERE, null, ex);
        } catch (IOException ex) {
            Logger.getLogger(AddHelicopterFXMLController.class.getName()).log(Level.SEVERE, null, ex);
        }
        Parent logIn = FXMLLoader.load(getClass().getResource("/aviationcompany/LogInFXML.fxml"));
        Scene logInScene = new Scene(logIn);
        Stage window = (Stage) body.getScene().getWindow();
        window.setScene(logInScene);
        window.setTitle("Aviation LogIn");
        window.show();

    }

    @Override
    public void initialize(URL location, ResourceBundle resources) {
        setClient();
    }

    private void setClient() {
        cl=(Client) Data.user;
    }

}
