import './App.css'
import { BrowserRouter as Router, Routes, Route, Navigate } from 'react-router-dom'
import Home from './pages/Home/Home'
import Settings from './pages/Settings/Settings'
import Stats from './pages/Stats/Stats'
import Setup from './pages/Setup/Setup'

function App() {

  return (
    <>
      <Router>
        <Routes>
          <Route path='/' element={<Home />} />
          <Route path='/settings' element={<Settings />} />
          <Route path='/stats' element={<Stats />} />
          <Route path='/setup' element={<Setup />} />
          <Route path='*' element={<Navigate to='/' />} />
        </Routes>
      </Router>
    </>
  )
}

export default App
