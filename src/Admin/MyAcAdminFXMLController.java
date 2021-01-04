package Admin;

import java.net.URL;
import java.util.ResourceBundle;
import javafx.event.ActionEvent;
import javafx.fxml.FXML;
import javafx.fxml.Initializable;
import javafx.scene.control.Button;
import javafx.scene.control.TextField;

/**
 * FXML Controller class
 *
 * @author Tanbin
 */
public class MyAcAdminFXMLController implements Initializable {

    @FXML
    private TextField userName;

    @FXML
    private TextField pass;

    @FXML
    private TextField cpass;

    @FXML
    private TextField email;

    @FXML
    private Button saveBtn;

    @FXML
    void saveBtnAction(ActionEvent event) {

    }
    @Override
    public void initialize(URL url, ResourceBundle rb) {
        // TODO
    }    
    
}
