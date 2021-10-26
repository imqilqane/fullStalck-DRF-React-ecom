import { Elements } from "@stripe/react-stripe-js"
import { loadStripe } from "@stripe/stripe-js"
import React from "react"
import Payment from "./Payment"

const PUBLIC_KEY = "pk_test_O0ZXmEZ8KcyfckwXk0w7iyY300a1SBfQ64"

const stripeTestPromise = loadStripe(PUBLIC_KEY)

export default function StripeContainer() {
	return (
		<Elements stripe={stripeTestPromise}>
			<Payment api_key={PUBLIC_KEY}/>
		</Elements>
	)
}
