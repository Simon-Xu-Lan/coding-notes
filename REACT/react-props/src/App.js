import React from 'react';
import Wrapper from './components/Wrapper';
import Title from './components/Title';
import Card from './components/Card';
// import SpongeBobCard from './components/SpongeBobCard';
// import SquidwardCard from './components/SquidwardCard';
// import MrKrabsCard from './components/MrKrabsCard';

function App() {
  let figures = [
    {
      name: 'Mr. Krabs1',
      occupation: 'Restaurant Owner',
      location: 'A Giant Anchor',
      src:
        'https://vignette3.wikia.nocookie.net/vsbattles/images/8/80/Mr._Krabs.png/revision/latest?cb=20150919162131',
    },
    {
      name: 'Squidward1',
      occupation: 'Cashier',
      location: 'An Easter Island Head',
      src:
        'https://vignette2.wikia.nocookie.net/fictionalcharacters/images/a/ac/Squidward.png/revision/latest?cb=20131121012626',
    },
    {
      name: 'SpongeBob1',
      occupation: 'Fry Cook',
      location: 'A Pinapple Under the Sea',
      src:
        'https://vignette.wikia.nocookie.net/spongebobgalaxy/images/0/07/SpongeBob_SquarePants.png/revision/latest?cb=20171228024014',
    },
  ];

  return (
    <Wrapper>
      <Title>Friends List</Title>
      {figures.map((figure) => {
        return <Card figure={figure} />;
      })}
    </Wrapper>
  );
}

export default App;
