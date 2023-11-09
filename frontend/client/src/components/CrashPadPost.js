import React, {useEffect, useState} from 'react'
import './CrashPadPost.css'
import AddCircleIcon from '@mui/icons-material/AddCircle';
import CrashPadPostCard from './CrashPadPostCard'
import NavBar from './NavBar'

function CrashPadPost() {
//   const [crashPosts, setCrashPosts] = useState([])
//   useEffect(() => {
//     fetch('/crashpads')
//     .then(response => response.json())
//     .then(crashPosts => console.log(setCrashPosts([...crashPosts].sort().reverse())))
// }, [])
const crashpadposts = [
  {
    "username": "freddyprice",
    "text": "Working a charter flight to Amsterdam next week ,any rooms available?",
    "location": "Amsterdam"
  },
  {
    "username": "emilydelta",
    "text": "Looking for A 2 night stay in Los Angeles, will take anything!",
    "location": "Los Angeles, California",
  },
  {
    "username": "samantharedding",
    "text": "Spare room available for the next week!",
    "location": "Los Angeles, CaliforniaHoboken, New Jersey",
  },
  {
    "username": "tiaholmes",
    "text": "I have a room avaiable for the next two days.",
    "location": "Philidelphia, Pennsylvania",
  },
  {
    "username": "kennyfranklin",
    "text": "Spare room in the best city in the world! For the next two days -",
    "location": "Miami, Florida",
  }
]
  return (
    <div>
        <NavBar />
        {/* {crashPosts.map((posts) => (<CrashPadPostCard key={posts.id} posts={posts} author={posts.author}/>))}
        <button className="add_post" >
        <AddCircleIcon />
        </button> */}
        <CrashPadPost crashpadposts={crashpadposts}/>
        </div>
    
    
  )
}

export default CrashPadPost;