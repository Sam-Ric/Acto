import './Activity.css';
import Application from '../Application/Application';

interface ActivityProps {
    name: string;
    apps: {
        activity_id: Number;
        name: string;
    }[];
};

export default function Activity({ name, apps }: ActivityProps) {
    return (
        <div className='activity'>
            <h3>{name}</h3>
            <div className='apps'>
                {apps.map((app) => {
                    return (
                        <Application activity_id={app.activity_id} name={app.name} />
                    );
                })}
            </div>
        </div>
    );
}