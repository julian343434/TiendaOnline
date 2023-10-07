import { useEffect, useState } from "react";
import { Link, useNavigate } from "react-router-dom";
import ItemLista from "./ItemLista";
import Lista from "./Lista";


const Home = () => {
    const usenavigate = useNavigate();
    const [customerlist, listupdate] = useState(null);
    const [displayusername, displayusernameupdate] = useState('');

    useEffect(() => {

        let username = sessionStorage.getItem('username');
        if (username === '' || username === null) {
            usenavigate('/login');
        } else {
            displayusernameupdate(username);
        }

    }, [])
    useEffect(() => {


        // let jwttoken = sessionStorage.getItem('jwttoken');
        // fetch("https://localhost:44308/Customer", {
        //     headers: {
        //         'Authorization': 'bearer ' + jwttoken
        //     }
        // }).then((res) => {
        //     return res.json();
        // }).then((resp) => {
        //     listupdate(resp);
        // }).catch((err) => {
        //     console.log(err.messsage)
        // });

    }, []);

    return (
        <div>
            <h1 className="text-center">{displayusername}</h1>
            <Lista user={displayusername}/>
        </div>
    );
}

export default Home;