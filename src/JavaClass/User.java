/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package JavaClass;

import java.io.Serializable;


/**
 *
 * @author Rakib
 */
public class User implements Serializable{
    private String userName,password,type;
    public String name,email;
    
    public String getUsername(){
        return userName;
    }
    
    public String getPass(){
        return password;
    }
    public User(String name,String userName, String pass,String email,String type){
        this.userName=userName;
        this.password=pass;
        this.type=type;
        this.name=name;
        this.email=email;

    }
}
