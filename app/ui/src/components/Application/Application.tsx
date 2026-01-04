import './Application.css';

interface AppProps {
    activity_id: Number;
    name: string;
}

export default function App({ activity_id, name }: AppProps) {
    return (
        <div className='application'>
            <p>{name}</p>
        </div>
    );
};