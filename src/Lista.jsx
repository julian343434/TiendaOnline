import React, { useState, useEffect } from 'react'
import ItemLista from './ItemLista';
export default function Lista({user}) {
    
    const [data, setData] = useState(null);

    async function loadData() {
        //const response = fetch("http://localhost:7201/json-data?name="+user);
        const response = fetch("http://localhost:1213/zapatos");
        const xd = (await response).json();
        return xd
    }


    useEffect(() => {
        loadData().then((res) => {
            setData(res);
        })
    }, [])

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
