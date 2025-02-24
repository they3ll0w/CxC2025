type CustomTooltipProps = {
    active: boolean;
    payload: any[];
    label: string;
}

export default function CustomTooltip({ active, payload, label }: CustomTooltipProps) {
    if (active && payload && payload.length) {
        const { event, time } = payload[0].payload
        return (
            <div className="bg-transparent px-2 py-1 border rounded-lg text-xs">
                <p className="dark:text-zinc-100 text-zinc-700">{event}</p>
                <p className="dark:text-zinc-400 text-zinc-500">{time} sec</p>
            </div>
        )
    }
    return null
}