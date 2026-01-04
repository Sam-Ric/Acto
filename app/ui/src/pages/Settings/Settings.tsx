import './Settings.css';
import Sidebar from '../../components/Sidebar/Sidebar';
import Activity from '../../components/Activity/Activity';
import { useSidebar } from '../../components/SidebarContext'; // Import the context

export default function Settings() {
    const { isSidebarExpanded } = useSidebar(); // Use the context

    // Example Activity List
    const work = {
        name: 'Work',
        apps: [
            { name: 'Code', activity_id: 1 },
            { name: 'Firefox', activity_id: 1 },
            { name: 'Slack', activity_id: 1 }
        ]
    };

    const gaming = {
        name: 'Gaming',
        apps: [
            { name: 'Battlefield 6', activity_id: 1 },
            { name: 'Fortnite', activity_id: 1 },
        ]
    };

    return (
        <div className='settings'>
            <Sidebar />
            <div className={`main ${isSidebarExpanded ? '' : 'collapsed'}`}>
                {/* Header */}
                <h2>Acto</h2>
                {/* List of settings */}
                <div className='entry'></div>
                {/* List of activities */}
                <h3>Activities</h3>
                <Activity name={work.name} apps={work.apps} />
                <Activity name={gaming.name} apps={gaming.apps} />
            </div>
        </div>
    );
}