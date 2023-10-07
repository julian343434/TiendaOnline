import React, { useState } from 'react';

const SearchBar = () => {
  const [searchTerm, setSearchTerm] = useState('');

  const handleInputChange = (event) => {
    setSearchTerm(event.target.value);
  };

  const handleFormSubmit = (event) => {
    event.preventDefault();
    // Aquí puedes hacer lo que necesites con el término de búsqueda, como enviarlo a una API o procesarlo de alguna otra manera
    console.log('Término de búsqueda:', searchTerm);
    setSearchTerm('');
  };

  return (
    <div>hola</div>
  );
};

export default Buscador;
