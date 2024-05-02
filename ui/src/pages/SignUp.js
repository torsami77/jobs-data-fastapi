import React, { useState } from 'react';
import { Button, TextField } from '@material-ui/core'
import '../styles/auth.css';
import { userTheme } from '../utilities/handlers';


function SignUp({role}) {
    userTheme(role);
    const [name, setName] = useState('')
    const [username, setUsername] = useState('')
    const [password, setPassword] = useState('')
    const [affiliation, setAffiliation] = useState('')


    const HandleChange = (e) => {
        const fieldName = e.target.name;
        const value = e.target.value;
        if(fieldName === 'name'){
          setName(value)
        }
        if(fieldName === 'username'){
            setUsername(value)
        }
        if(fieldName === 'password'){
            setPassword(value)
        }
        if(fieldName === 'affiliation'){
            setAffiliation(value)
        }
    }

    return (
        <div className="Container">
            <p>
                {role === "employee" ? "Employee Sign Up" : "Customer Sign Up"}
            </p>
            < TextField 
                className="Form-Element"
                variant="outlined"
                value={name}
                name="name"
                label="name   (required)"
                onChange={(e) => {HandleChange(e)}}
                required
            />
            < TextField 
                className="Form-Element"
                variant="outlined"
                value={username}
                name="username"
                label="username   (required)"
                onChange={(e) => {HandleChange(e)}}
                required
            />
            < TextField 
                className="Form-Element"
                variant="outlined"
                value={password}
                name="password"
                label="password   (required)"
                onChange={(e) => {HandleChange(e)}}
                required
            />
            < TextField 
                className="Form-Element"
                variant="outlined"
                value={affiliation}
                name="affiliation"
                label="affiliation   (required)"
                onChange={(e) => {HandleChange(e)}}
                required
            />
            <Button type="submit" variant="contained" color="default" className="Form-Element" >
                Sign Up
            </Button>
            <p>
                <a href="/sign-in">Go to Sign-in page</a>
            </p>
        </div>
  );
}

export default SignUp;
