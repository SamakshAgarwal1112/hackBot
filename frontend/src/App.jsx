import './App.css'
import React, {useState, useEffect} from 'react'
import axios from 'axios'

function App() {
  const [events,setEvents] = useState([]);
  const [loading,setLoading] = useState(true)

  useEffect(()=>{
    try {
      axios.get('http://127.0.0.1:8000/api/events/hackathons/').then((res)=>{
        setEvents(res.data)
        setLoading(false)
      })
    } catch (error) {
      console.log(error)
      setLoading(true)
    }
  },[])

  return (
    <div>
      <h1>Events</h1>
      {
        loading?
        <p>Fetching data...</p>:
        <div>
              <table>
                <thead>
                  <tr>
                    <td>Number</td>
                    <td>Title</td>
                    <td>Date</td>
                    <td>Url</td>
                    <td>Location</td>
                    <td>Mode</td>
                  </tr>
                </thead>
                <tbody>
                {
                  events.map((event,index)=>(
                    <tr key={index} >
                      <td>
                        <p>
                          {index+1}
                        </p>
                      </td>
                      <td>
                        <p>
                          {event.title}
                        </p>
                      </td>
                      <td>
                        <p>
                          {event.date}
                        </p>
                      </td>
                      <td>
                        <a href={event.url} target='_blank'>
                          {event.url}
                        </a>
                      </td>
                      <td>
                        <p>
                          {event.location}
                        </p>
                      </td>
                      <td>
                        <p>
                          {event.mode}
                        </p>
                      </td>
                    </tr>
                  ))
                }
                </tbody>
              </table>
        </div>
      }
      
    </div>
  )
}

export default App
