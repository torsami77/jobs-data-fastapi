import React, { useState } from 'react';
import { Button, TextField } from '@material-ui/core'
import '../styles/auth.css';
import '../App.css';


function Index() {
    const [username, setUsername] = useState('')
    const [password, setPassword] = useState('')

    const HandleChange = (e) => {
        const fieldName = e.target.name;
        const value = e.target.value;
        if(fieldName === 'username'){
            setUsername(value)
        }
        if(fieldName === 'password'){
            setPassword(value)
        }
    }

    return (
        <div className="Container">
             <p>
                Sign In
            </p>
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
            <Button type="submit" variant="contained" color="default" className="Form-Element" >
                Sign In
            </Button>
            <p>
                <a href="/sign-up">Got to Sign-up</a>
            </p>
        </div>
    );
}

export default Index;
