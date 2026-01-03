import { useState } from 'react';
import './Home.css';
import Sidebar from '../../components/Sidebar/Sidebar';
import Switch from '../../components/Switch/Switch';

export default function Home() {
    const [isSidebarExpanded, setIsSidebarExpanded] = useState(true);
    const [monitorStatus, setMonitorStatus] = useState(false);

    return (
        <div className='home'>
            <Sidebar onToggle={(expanded) => setIsSidebarExpanded(expanded)} />
            <div className={`main ${isSidebarExpanded ? '' : 'collapsed'}`}>
                <h2>Acto</h2>
                <Switch onToggle={(monitorStatus) => setMonitorStatus(monitorStatus)}/>
                <p>Activity monitor is {monitorStatus ? 'enabled' : 'disabled'}</p>
            </div>
        </div>
    );
}