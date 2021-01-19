/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package Client;

import JavaClass.Client;
import JavaClass.Data;
import JavaClass.Helicopter;
import JavaClass.LendingCompany;
import java.io.File;
import java.io.FileNotFoundException;
import java.net.URL;
import java.time.LocalDate;
import java.util.ArrayList;
import java.util.ResourceBundle;
import java.util.Scanner;
import java.util.logging.Level;
import java.util.logging.Logger;
import javafx.collections.FXCollections;
import javafx.collections.ObservableList;
import javafx.event.ActionEvent;
import javafx.fxml.FXML;
import javafx.fxml.Initializable;
import javafx.scene.control.DatePicker;
import javafx.scene.control.TableColumn;
import javafx.scene.control.TableView;
import javafx.scene.control.TextField;
import javafx.scene.control.cell.PropertyValueFactory;

/**
 * FXML Controller class
 *
 * @author Rakib
 */
public class AddBookingFXMLController implements Initializable {

    @FXML
    private TextField hModel;
    @FXML
    private TextField pickLoc;
    @FXML
    private TextField desLoc;
    @FXML
    private DatePicker pickDate;
    @FXML
    private TextField time;
    @FXML
    private TableView<Helicopter> table;
    @FXML
    private TableColumn<Helicopter, String> model;
    @FXML
    private TableColumn<Helicopter, String> maxPasCap;
    @FXML
    private TableColumn<Helicopter, String> maxW;
    @FXML
    private TableColumn<Helicopter, String> aDate;

    /**
     * Initializes the controller class.
     */
    @Override
    public void initialize(URL url, ResourceBundle rb) {
        pTable();
       
        
        // TODO
    }    
    public void pTable(){
//        TableView<Helicopter> table=new TableView();
//        TableColumn<Helicopter, String> model= new TableColumn<>("Model");
//        TableColumn<Helicopter,String> maxPasCap= new TableColumn<>("Passanger Capacity");;
//        TableColumn<Helicopter,String> maxW= new TableColumn<>("Maximum Weight");;
//        TableColumn<Helicopter, String>  aDate= new TableColumn<>("Avaiable Date");;
        
        
        //set up the columns in the table
        model.setCellValueFactory(new PropertyValueFactory<>("model"));
        maxPasCap.setCellValueFactory(new PropertyValueFactory<>("maxPassCap"));
        maxW.setCellValueFactory(new PropertyValueFactory<>("maxWeight"));
        aDate.setCellValueFactory(new PropertyValueFactory<>("aDate"));
        ArrayList<Helicopter>data=new ArrayList<>();
        File file = new File("helicopter.txt");
         
        try {
            Scanner sc = new Scanner(file);
            while (sc.hasNextLine()) {                
                String []dataArr=sc.nextLine().split(",");
                Helicopter h=new Helicopter(dataArr[0], dataArr[1], dataArr[2], dataArr[3]);
                data.add(h);
            }
        } catch (FileNotFoundException ex) {
            Logger.getLogger(AddBookingFXMLController.class.getName()).log(Level.SEVERE, null, ex);
        }
        
        ObservableList<Helicopter> ol=FXCollections.observableArrayList(data);
        table.setItems(ol);
        table.getColumns().addAll(model,maxPasCap,maxW,aDate);
    }

    @FXML
    private void addBtn(ActionEvent event) {
        Client cl =(Client)Data.user;
        String s="Pending";
        cl.addBooking(hModel.getText(), pickLoc.getText(), desLoc.getText(), time.getText(),pickDate.getValue(),s);
        Data.user=cl;
        hModel.setText("");
        pickLoc.setText("");
        desLoc.setText("");
        time.setText("");
    }
    
}
