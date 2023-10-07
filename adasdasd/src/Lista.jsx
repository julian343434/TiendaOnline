import React, { useState, useEffect } from 'react'
import ItemLista from './ItemLista';
export default function Lista({user}) {
    
    const [data, setData] = useState(null);

    async function loadData() {
        //const response = fetch("http://localhost:7201/json-data?name="+user);
        if (user == "deivid") {
            const response = fetch("http://localhost:1213/deivid");
            const xd = (await response).json();
            return xd
        }else if (user == "marlon" ){
            const response = fetch("http://localhost:1213/marlon");
            const xd = (await response).json();
            return xd
        }else if (user == "carlos" ){
            const response = fetch("http://localhost:1213/carlos");
            const xd = (await response).json();
            return xd
        }else if (user == "yeiner" ){
            const response = fetch("http://localhost:1213/yeiner");
            const xd = (await response).json();
            return xd
        }else if (user == "hermes" ){
            const response = fetch("http://localhost:1213/hermes");
            const xd = (await response).json();
            return xd
        }
    }
    
    console.log("no se encontro la data");

    useEffect(() => {
        loadData().then((res) => {
            setData(res);
        })
    })

    return (
        <div className='item-list'>
            {data == null ? (null) : (
                data.map((e) => {
                    return <ItemLista data={e} />
                })
            )}
        </div>
    )
}
