"use client"
import MainLayout from "../main/layout"
import { useState } from "react";

import {
    Command,
    CommandEmpty,
    CommandGroup,
    CommandInput,
    CommandItem,
    CommandList,
    CommandSeparator,
    CommandShortcut,
} from "@/components/ui/command"
import { Button } from "@/components/ui/button";

const eventTypes = [
    "session_end",
    "application-window-opened",
    "dashboard:my-book::view",
    "dashboard:my-book:layout:render",
    "dashboard:my-book:widget:render",
    "dashboard:my-book:configurable-table:render",
    "triaged-submission-list:my-book::view",
    "triaged-submission-list:my-book:configurable-table:render",
    "session_start",
    ":all-accounts:configurable-table:render",
    ":all-accounts:widget:render",
    ":all-accounts:layout:render",
    ":all-accounts::view",
    "account-lines::layout:render",
    "account-lines:::view",
    "account:::view",
    "account-lines::widget:render",
    "account-lines::configurable-table:render",
    "::nav-header:action-center-click",
    "action-center:::view",
    "action-center:::close-click",
    "account-auto-rating::configurable-table:render",
    "account-auto-rating:::view",
    "account-lines:::change-rating-click",
    "account-property-rating:perils:configurable-table:render",
    "account-property-rating:perils::view",
    "account-property-rating:perils:perils-table:add-click",
    "account-property-rating:perils:perils-table:edit-click",
    "action-center:::submit-click",
    "action-center:action-details::view",
    "dashboard:my-book::action-click",
    "action-center:action-details:response-form:submit-click",
    "submissions:all-auto::view",
    "submissions:all-auto:configurable-table:render",
    "submissions:all-policy::view",
    "submissions:policy-create::view",
    "submissions:triaged_submissions-definition::view",
    "triaged-submission:triaged_submissions-definition::view",
    "triaged-submission:triaged_submissions-definition:layout:render",
    "triaged-submission:triaged_submissions-definition:widget:render",
    "triaged-submission-list:triaged_submissions-definition:configurable-table:render",
    "triaged-submission-list:triaged_submissions-definition::view",
    "submissions:all-policy:configurable-table:render",
    "submissions:all-terrorism::view",
    "::configurable-table:render",
    "account-lines::duplicate-policy-modal:duplicate-rating",
    "account-property-rating:perils:model-request-details:save-click",
    "dashboard:portfolio-insights:layout:render",
    "dashboard:portfolio-insights::view",
    "dashboard:portfolio-insights:widget:render",
    "all-accounts:renewals:layout:render",
    "all-accounts:renewals::view",
    "agency-dashboard:::view",
    "agency-dashboard::layout:render",
    "agency-dashboard::widget:render",
    "agency-dashboard::configurable-table:render",
    "account-lines::templeton-docs:create-document-click",
    "account-lines::construction-excess-rater:save-new-quote-click",
    "account-lines::construction-excess-rater:create-document-click",
    "dashboard:my-book:recent-actions-table:action-click",
    "dashboard:my-book:recent-actions-table:account-click",
    "account-property-rating:perils:layers:add-click",
    "account-property-rating:perils:layers:delete-click",
    "assigned-email-thread:::email-thread-expansion",
    "::widget:render",
    "goals-and-rules:goals:configurable-table:render",
    "goals-and-rules:goals::view",
    "submissions:policy-definition::view",
    "submissions:policy-definition::submit-click",
    "submissions:all-ingest_policy_through_pd:configurable-table:render",
    "submissions:all-ingest_policy_through_pd::view",
    "submissions:ingest_policy_through_pd-create::view",
    "submissions:all-account:configurable-table:render",
    "submissions:all-account::view",
    "all-accounts:new-business:layout:render",
    "all-accounts:new-business::view",
    "all-accounts:new-business:accounts-table:account-click",
    "::nav-header:user-signed-out",
    "account-broker-readonly-view::layout:render",
    "account-broker-readonly-view:::view",
    "account-broker-readonly-view::widget:render",
    "account-broker-readonly-view::configurable-table:render",
    "::duplicate-policy-modal:duplicate-rating",
    "::nav-header:help-menu-opened",
    "submissions:policy-definition:configurable-table:render",
    "account-property-rating:pricing-detail:configurable-table:render",
    "account-property-rating:pricing-detail::view",
    "account-property-rating:pricing-detail::open-ra-file-click",
    "submissions:all-exposures::view",
    "submissions:all-exposures:configurable-table:render",
    "submissions:policy-create:configurable-table:render",
    "submissions:policy-create::submit-click",
    "submissions:exposures-create::view",
    "submissions:exposures-create::submit-click",
    "::layout:render",
    "account-property-rating::configurable-table:render",
    "classification-rules::configurable-table:render",
    "brokerage::configurable-table:render",
    "contacts::configurable-table:render",
    "brokerage::layout:render",
    "brokerage:::view",
    "brokerage::widget:render",
    "carriers::configurable-table:render",
    "account-property-rating:::change-rating-click",
    "submissions:auto-create::view",
    "account-workers-comp-rating:::view",
    "submissions:all-exposure_demo::view",
    "submissions:all-exposure_demo:configurable-table:render",
    "submissions:exposure_demo-create::view",
    "submissions:all-justin_test_submission::view",
    "submissions:all-old_renewal::view",
    "submissions:old_renewal-create::view",
    "submissions:all-financial_lines::view",
    "submissions:all-financial_lines:configurable-table:render",
    "agency-account::layout:render",
    "agency-account:::view",
    "agency-account::widget:render",
    "agency-account::configurable-table:render",
    "submissions:financial_lines-create::view",
    "account-broker-view::layout:render",
    "account-broker-view:::view",
    "account-broker-view::widget:render",
    "account-broker-view::configurable-table:render",
    "submissions:all-renewal::view",
    "submissions:renewal-create::view",
    "submissions:renewal-create::submit-click",
    "submissions:all-renewal:configurable-table:render",
    "submissions:renewal-definition::view",
    "submissions:all-generic_submission::view",
    "account-lines::construction-excess-rater:modify-existing-quote-click",
    "all-accounts:new-business:configurable-table:render",
    "all-accounts:new-business:widget:render",
    "account-lines:::action-center-click",
    "submissions:exposures-definition::view",
    "triaged-submission:triaged_submissions-definition::winnability-click",
    "triaged-submission:triaged_submissions-definition::appetite-click",
    "goals-and-rules:rules:configurable-table:render",
    "goals-and-rules:rules::view",
    "linked-email-thread-attachments:triaged_submissions-definition::document-download-click",
    "complex-rules::configurable-table:render",
    "submissions:account-create::view",
    "goals-and-rules:goal-definition::view",
    "goals-and-rules:edit-goal::view",
    "goals-and-rules:edit-goal::advanced-filters-applied",
    "goals-and-rules:goal-definition::delete-click",
    "goals-and-rules:edit-goal::save-click",
    "all-accounts:renewals:configurable-table:render",
    "all-accounts:renewals:widget:render"
]


export default function Predict() {
    const [selectedEvents, setSelectedEvents] = useState<string[]>([])
    const [prediction, setPrediction] = useState<string | null>(null)
    const [confidence, setConfidence] = useState<string | null>(null)
    const [endsech, setEndsesh] = useState<string | null>(null)

    const toggleEvent = (event: string) => {
        setSelectedEvents((prev) =>
            prev.includes(event)
                ? prev.filter((e) => e !== event)
                : [...prev, event]
        );
    };

    const submitEvents = async () => {
        try {
            console.log(selectedEvents)

            const response = await fetch("http://localhost:4000/api/v1/predict", {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({ sequence: selectedEvents }),
            });
            console.log(response)

            if (!response.ok) throw new Error("Failed to fetch prediction")

            const data = await response.json()
            console.log(data)
            setPrediction(data.predicted_event)
            setConfidence(data.prob_event)
            setEndsesh(data.prob_end_session)
        } catch (error) {
            console.error(error)
            setPrediction("Error predicting event.")
        }
    };

    return (
        <MainLayout>
            <div className="h-full grid grid-rows-11 justify-items-center dark:bg-zinc-800 overflow-auto p-4">
                <h1 className="row-span-1 text-xl font-bold">Select events to predict the next one</h1>

                <div className="row-span-8 grid grid-cols-3 gap-2 w-full">

                    <Command className="col-span-2 rounded-lg dark:bg-zinc-300 dark:text-zinc-800 border dark:border-zinc-600 border-zinc-300 shadow-md md:min-w-[450px]">
                        <CommandInput className="text-zinc-600" placeholder="Type an event or search..." />
                        <CommandList>
                            <CommandEmpty>No results found.</CommandEmpty>
                            <CommandGroup heading="Events">
                                {eventTypes.map((event) => (
                                    <CommandItem key={event} onSelect={() => toggleEvent(event)}>
                                        <span className="text-xs">{event}</span>
                                    </CommandItem>
                                ))}
                            </CommandGroup>
                        </CommandList>
                    </Command>

                    <div className="col-span-1 flex flex-col justify-between bg-gray-200 dark:bg-zinc-700 rounded-md shadow-md">
                        <div className="p-4">
                            <h2 className="font-semibold">Selected Events:</h2>
                            <ul className="overflow-auto">
                                {selectedEvents.map((event) => (
                                    <li
                                        key={event}
                                        className="cursor-pointer text-xs p-2 bg-gray-300 dark:bg-zinc-600 rounded mt-2 hover:bg-zinc-400 dark:hover:bg-zinc-800"
                                        onClick={() => toggleEvent(event)}
                                    >
                                        {event}
                                    </li>
                                ))}
                            </ul>
                        </div>
                        <Button
                            className="bg-fuchsia-700 hover:bg-fuchsia-800"
                            onClick={submitEvents}
                            disabled={selectedEvents.length === 0}>
                            Predict
                        </Button>
                    </div>

                </div>

                {prediction && (
                    <div className="flex flex-col justify-center row-span-2 text-xs mt-2 px-4 py-2 bg-green-200 dark:bg-green-700 text-green-900 dark:text-green-200 rounded shadow-md max-w-[70%]">
                        <p><span className="font-semibold">Predicted Next Event: </span>{prediction}</p>
                        <p>Confidence level: {confidence}</p>
                        <p>Probability of ending the session: {endsech}</p>
                    </div>
                )}

            </div>

        </MainLayout>
    )
}