package LendingCompany;

import JavaClass.LendingCompany;
import JavaClass.Data;
import JavaClass.Helicopter;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.ObjectInputStream;
import java.io.ObjectOutputStream;
import java.net.URL;
import java.time.LocalDate;
import java.util.Observable;
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
import javafx.scene.control.Label;
import javafx.scene.control.Menu;
import javafx.scene.control.MenuItem;
import javafx.scene.control.ScrollPane;
import javafx.scene.control.TableColumn;
import javafx.scene.control.TableView;
import javafx.scene.control.cell.PropertyValueFactory;
import javafx.scene.control.cell.TextFieldTableCell;
import javafx.scene.layout.AnchorPane;
import javafx.stage.Stage;

public class LendingCompanyFXMLController implements Initializable{

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
    private Label userName;
    LendingCompany lc;
    void setUser(){
        userName.setText(userName.getText()+Data.user.name);
        lc=(LendingCompany) Data.user;
        
    }
    void helicopInfoTable(){
        TableView<Helicopter> tableView=new TableView();
        TableColumn<Helicopter, String> model= new TableColumn<>("Model");
        TableColumn<Helicopter,String> passengerCapacity = new TableColumn<>("Passanger Capacity");
        TableColumn<Helicopter,String> maxWeight= new TableColumn<>("Maximum Weight");
        TableColumn<Helicopter, LocalDate> avialableData= new TableColumn<>("Avaiable Date");
        //set up the columns in the table
        model.setCellValueFactory(new PropertyValueFactory<>("model"));
        passengerCapacity.setCellValueFactory(new PropertyValueFactory<>("maxPassCap"));
        maxWeight.setCellValueFactory(new PropertyValueFactory<>("maxWeight"));
        avialableData.setCellValueFactory(new PropertyValueFactory<>("availableDate"));
        lc=(LendingCompany) Data.user;
        ObservableList<Helicopter> ol=FXCollections.observableArrayList(lc.helicopteList);
        tableView.setItems(ol);
        tableView.getColumns().addAll(model,passengerCapacity,maxWeight,avialableData);
        tableView.setEditable(true);
        model.setCellFactory(TextFieldTableCell.forTableColumn());
        
        body.setContent(tableView);

    
    }
    @FXML
    void aboutAction(ActionEvent event) throws IOException {
        FXMLLoader loader=new FXMLLoader();
        loader.setLocation(getClass().getResource("/aviationcompany/AboutFXML.fxml"));
        AnchorPane pane = loader.load();
        body.setContent(pane);

    }

    @FXML
    void addHelicopterA(ActionEvent event) throws IOException {
        FXMLLoader loader=new FXMLLoader();
        loader.setLocation(getClass().getResource("AddHelicopterFXML.fxml"));
        AnchorPane pane = loader.load();
        AddHelicopterFXMLController ah=loader.getController();
        
        body.setContent(pane);
        
    }

    @FXML
    
    void bookingConfirmationA(ActionEvent event) {
       
           
    }
    

    @FXML
    void goHomeAction(ActionEvent event) throws IOException {
        AnchorPane pane = FXMLLoader.load(getClass().getResource("AddHelicopterFXML.fxml"));
        body.setContent(pane);

    }

    @FXML
    void logOut(ActionEvent event) throws IOException {
         try {
            ObjectOutputStream os=new ObjectOutputStream(new FileOutputStream(lc.getUsername()+".bin"));
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

    @FXML
    void viewDelHelicopterAction(ActionEvent event) {
       helicopInfoTable();

    }

    @Override
    public void initialize(URL location, ResourceBundle resources) {
        setUser();
    }

    @FXML
    private void modifyHelicop(ActionEvent event) {
        helicopInfoTable();
    }
    

}
