import { useEffect, useState } from "react";
import zapato1 from './imagenes/Reebok negra.jpg';

export default function iteamLista({data}) {
    return (
        <div className="item">
            <div>{data.nombre}</div>
            <img src={"./"+data.nombre+".jpeg"} alt="" />
        </div>
    );
}
