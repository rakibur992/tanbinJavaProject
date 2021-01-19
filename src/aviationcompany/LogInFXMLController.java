/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package aviationcompany;

import JavaClass.Admin;
import JavaClass.Client;
import JavaClass.LendingCompany;
import JavaClass.Data;
import JavaClass.User;
import LendingCompany.AddHelicopterFXMLController;
import LendingCompany.LendingCompanyFXMLController;
import MD5.MD5;
import java.io.File;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.FileWriter;
import java.io.IOException;
import java.io.ObjectInputStream;
import java.io.ObjectOutputStream;
import java.net.URL;
import java.util.ResourceBundle;
import java.util.Scanner;
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
import javafx.scene.control.Label;
import javafx.scene.control.PasswordField;
import javafx.scene.control.TextField;
import javafx.scene.input.MouseEvent;
import javafx.scene.layout.AnchorPane;
import javafx.stage.Stage;

/**
 *
 * @author Tanbin
 */
public class LogInFXMLController implements Initializable {

    @FXML
    private AnchorPane logInPane;

    @FXML
    private TextField userID;

    @FXML
    private PasswordField pass;

    @FXML
    private Button login;

    @FXML
    private Button register;
    @FXML
    private Label error;

    @FXML

    void handleLogInBtn(ActionEvent event) throws IOException {

        File file = new File("user.txt");
        Scanner sc = new Scanner(file);
        MD5 md5 = new MD5();
        String data;
        while (sc.hasNextLine()) {
            data = sc.nextLine();
            String[] dataArr = data.split(",");
            String pass_check = md5.getMd5(pass.getText());
            FXMLLoader loader = new FXMLLoader();

            if (dataArr[1].equals(userID.getText()) && dataArr[2].equals(pass_check)) {
                try {
                    ObjectInputStream is = new ObjectInputStream(new FileInputStream(dataArr[1] + ".bin"));
                    Data.user = (User) is.readObject();

                } catch (FileNotFoundException ex) {
                    switch (dataArr[4]) {
                        case "admin": {
                            Admin user = new Admin(dataArr[0], dataArr[1], dataArr[2], dataArr[3], dataArr[4]);
                            ObjectOutputStream os =new ObjectOutputStream(new FileOutputStream(dataArr[1]+".bin"));
                            os.writeObject(user);
                            Data.user=user;
                            break;
                        }

                        case "management": {

                            break;
                        }
                        case "client": {
                            Client user = new Client(dataArr[0], dataArr[1], dataArr[2], dataArr[3], dataArr[4]);
                            ObjectOutputStream os =new ObjectOutputStream(new FileOutputStream(dataArr[1]+".bin"));
                            os.writeObject(user);
                            Data.user=user;

                            break;
                        }
                        case "lendingCompany": {
                            LendingCompany user = new LendingCompany(dataArr[0], dataArr[1], dataArr[2], dataArr[3], dataArr[4]);              
                            ObjectOutputStream os =new ObjectOutputStream(new FileOutputStream(dataArr[1]+".bin"));
                            os.writeObject(user);
                            Data.user=user;

                            break;
                        }
                        case "pilot": {

                            break;
                        }

                    }
                } catch (IOException ex) {
                    Logger.getLogger(AddHelicopterFXMLController.class.getName()).log(Level.SEVERE, null, ex);
                } catch (ClassNotFoundException ex) {
                    Logger.getLogger(AddHelicopterFXMLController.class.getName()).log(Level.SEVERE, null, ex);
                }

                switch (dataArr[4]) {
                    case "admin": {
                        loader.setLocation(getClass().getResource("/Admin/AdminFXML.fxml"));
                        Parent admin = loader.load();
                        Scene adminScene = new Scene(admin);
                        Stage window = (Stage) ((Node) event.getSource()).getScene().getWindow();
                        window.setScene(adminScene);
                        window.setTitle("Aviation Admin");
                        window.show();
                        break;
                    }

                    case "management": {

                        loader.setLocation(getClass().getResource("/BookingManagement/BookingManagementFXML.fxml"));
                        Parent admin = loader.load();
                        Scene adminScene = new Scene(admin);
                        Stage window = (Stage) ((Node) event.getSource()).getScene().getWindow();
                        window.setScene(adminScene);
                        window.setTitle("Aviation Managment");
                        window.show();
                        break;
                    }
                    case "client": {

                        loader.setLocation(getClass().getResource("/Client/ClientFXML.fxml"));
                        Parent admin = loader.load();
                        Scene adminScene = new Scene(admin);
                        Stage window = (Stage) ((Node) event.getSource()).getScene().getWindow();
                        window.setScene(adminScene);
                        window.setTitle("Aviation  Client");
                        window.show();
                        break;
                    }
                    case "lendingCompany": {
                        
                        loader.setLocation(getClass().getResource("/LendingCompany/LendingCompanyFXML.fxml"));
                        Parent admin = loader.load();
                        Scene adminScene = new Scene(admin);
                        Stage window = (Stage) ((Node) event.getSource()).getScene().getWindow();
                        window.setScene(adminScene);
                        window.setTitle("Aviation Lending Company");
                        window.show();
                        break;
                    }
                    case "pilot": {

                        loader.setLocation(getClass().getResource("/Pilot/PilotFXML.fxml"));
                        Parent admin = loader.load();
                        Scene adminScene = new Scene(admin);
                        Stage window = (Stage) ((Node) event.getSource()).getScene().getWindow();
                        window.setScene(adminScene);
                        window.setTitle("Aviation Pilot");
                        window.show();
                        break;
                    }

                }

            }
        }
        error.setText("Username/Password Incorrect");

//        MD5 md5=new MD5();
//        System.out.println(md5.getMd5(pass.getText()));
    }

    @FXML

    void handleRegBtn(ActionEvent event) throws IOException {
        Parent reg = FXMLLoader.load(getClass().getResource("RegisterFXML.fxml"));
        Scene regScene = new Scene(reg);
        Stage window = (Stage) ((Node) event.getSource()).getScene().getWindow();
        window.setScene(regScene);
        window.setTitle("Client Registration");
        window.show();

//        AnchorPane regPane = FXMLLoader.load(getClass().getResource("RegisterFXML.fxml"));
//        logInPane.getChildren().setAll(regPane);
    }

    @Override
    public void initialize(URL url, ResourceBundle rb) {
        // TODO
    }

    @FXML
    private void errorDis(MouseEvent event) {
        error.setText("");

    }

}
