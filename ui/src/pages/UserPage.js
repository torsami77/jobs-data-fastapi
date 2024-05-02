import React, { useState } from 'react';
import { Button, TextField } from '@material-ui/core'
import '../styles/userpage.css';
import { userTheme } from '../utilities/handlers';


function UserPage({role}) {
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
                Task Board
            </p>
            <div className='board'>
                <div id="in-progress">
                    <span> In progress</span>
                    <div className="content">
                        <div className="task">
                            <span>
                                Lorem ipsum dolor sit amet consectetur adipisicing elit. Maxime mollitia, Lorem ipsum dolor sit amet consectetur adipisicing elit. Maxime mollitia,
                                molestiae quas vel sint commodi repudiandae consequuntur voluptatum laborum
                                numquam blanditiis harum quisquam                        
                            </span>
                        </div>
                    </div>
                </div>

                <div id="in-review">
                    <span> In review</span>
                    <div className="content">

                    </div>
                </div>

                <div id="done">
                    <span>Done</span>
                    <div className="content">

                    </div>
                </div>
            </div>
            
           
        </div>
  );
}

export default UserPage;
