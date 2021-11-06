import React from 'react';
import FriendCard from './components/FriendCard';
import Wrapper from './components/Wrapper';
import friends from './friends.json';
import './App.css';

class App extends React.Component {
  state = {
    // equalivent to friends: friends
    friends,
  };

  removeFriend = (id) => {
    console.log(id);
    this.setState({
      friends: this.state.friends.filter((friend) => friend.id !== id),
    });
  };

  render() {
    return (
      <Wrapper>
        <h1 className="title">Friends List</h1>
        {this.state.friends.map((friend) => (
          <FriendCard
            removeFriend={this.removeFriend}
            id={friend.id}
            name={friend.name}
            image={friend.image}
            occupation={friend.occupation}
            location={friend.location}
          />
        ))}
      </Wrapper>
    );
  }
}

export default App;
