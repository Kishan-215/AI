import nltk
from nltk.chat.util import Chat, reflections

nltk.download('punkt')

pairs = [
    ["hello|hi|hey", ["Hi there! How can I help you today?", "Hello!"]],
    [r"(.*)problem(.*)", ["Could you please specify the problem area (e.g., order status, payment method)?"]],
    ["How can I return a product?", ["To initiate a return, please visit our 'Returns' page on the website or contact our support team for assistance."]],
    ["I received a damaged product", ["I apologize for the inconvenience. Please provide your order number, and we will arrange for a replacement or refund."]],
    ["Tell me about your shipping options", ["We offer standard and express shipping. The delivery time and cost depend on your location. You can find more details on our 'Shipping' page."]],
    ["What is the status of my refund?", ["To check the status of your refund, please provide the reference number or the email associated with your order."]],
    ["Can I change my shipping address?", ["Certainly! Please contact our support team as soon as possible with the updated shipping address."]],
    ["I can't log in to my account", ["If you're having trouble logging in, you can use the 'Forgot Password' link on the login page or contact support for assistance."]],
    ["Tell me about your loyalty program", ["Our loyalty program offers exclusive rewards and discounts. You can find more information on our website or contact support for details."]],
    ["I have a suggestion", ["We appreciate your feedback! Please share your suggestion, and we'll consider it for future improvements."]],
    ["How can I check the warranty status?", ["To check the warranty status of your product, provide the serial number, and we'll provide you with the relevant information."]],
    ["Can I change my order after placing it?", ["To make changes to your order, please reach out to our support team within a few hours of placing the order."]],
    ["I'm having trouble applying a discount code", ["Ensure that the discount code is entered correctly and is still valid. If the issue persists, contact our support team for assistance."]],
    ["What security measures do you have for online transactions?", ["We use encryption and secure protocols to ensure the safety of your online transactions. Your security is our priority."]],
    ["Can you recommend product alternatives?", ["Certainly! Please specify the type of product you're looking for, and we'll suggest some alternatives from our catalog."]],
    ["order status", ["Your order is currently being processed."]],
    ["payment issue", ["Please contact our support team at support@example.com for assistance with payment issues."]],
    ["goodbye", ["Goodbye! Have a great day."]],
    ["How can I contact customer support?", ["You can contact our support team via email at support@example.com or by phone at 123-456-7890."]],
    ["What are your business hours?", ["Our business hours are from 9 AM to 5 PM, Monday to Friday."]],
    ["Can you help me track my order?", ["Certainly! To track your order, please provide your order number."]],
    ["What is your return policy?", ["Our return policy allows returns within 30 days of purchase. Please check our website for detailed information."]],
    ["How do I reset my password?", ["You can reset your password by clicking on the 'Forgot Password' link on the login page."]],
    ["What payment methods do you accept?", ["We accept credit cards (Visa, MasterCard, American Express) and PayPal."]],
    ["Is there a warranty for the products?", ["Yes, our products come with a standard one-year warranty. Please check the product documentation for details."]],
    ["How do I cancel or modify my order?", ["To cancel or modify your order, please contact our support team as soon as possible."]],
    ["Do you offer discounts or promotions?", ["Yes, we regularly have promotions and discounts. Check our website or subscribe to our newsletter for updates."]],
    ["Can you provide technical support for your products?", ["Certainly! Please describe the technical issue you are facing, and we'll do our best to assist you."]],
    ["How do I apply a discount code during checkout?", ["During checkout, you can enter the discount code in the designated field before completing your purchase."]],
    ["Can you recommend accessories for my product?", ["Certainly! Please provide the name or model of your product, and we can suggest compatible accessories."]],
    ["How do I check the status of a repair or service request?", ["To check the status of a repair or service request, please provide the reference number, and we'll provide you with an update."]],
    ["Can I speak to a supervisor or manager?", ["Certainly! Please hold on, and I will transfer you to a supervisor."]],
    ["What is your policy on product recalls?", ["In the event of a product recall, we will notify affected customers and provide instructions on returning or replacing the product."]],
    ["How do I unsubscribe from marketing emails?", ["To unsubscribe from marketing emails, you can click on the 'Unsubscribe' link at the bottom of any marketing email you receive from us."]],
    ["How do I obtain a refund for a digital purchase?", ["For digital purchases, refunds are typically handled based on our digital product refund policy. Please check our website for details."]],
    ["Tell me about your customer rewards program", ["Our customer rewards program offers points for every purchase, which you can redeem for discounts on future orders. Check your account for points balance."]],
    ["What is the expiration date of my gift card?", ["To check the expiration date of your gift card, please provide the card number, and we'll provide you with the relevant information."]],
    ["How do I subscribe to your newsletter?", ["You can subscribe to our newsletter on our website by entering your email in the 'Subscribe' section. Stay tuned for updates and exclusive offers!"]],
    ["I have a complaint", ["I'm sorry to hear that. Please share the details of your complaint, and we'll do our best to address and resolve the issue."]],
    ["Tell me about your product testing process", ["Our products undergo rigorous testing to ensure quality and safety. We prioritize delivering reliable products that meet the highest standards."]],
    ["How can I provide feedback on your website?", ["We appreciate your feedback! You can submit your feedback through the 'Contact Us' page on our website. Thank you for helping us improve!"]],
    ["Can I change the color/size of my ordered item?", ["To change the color or size of your ordered item, contact our support team, and they will assist you with the necessary steps."]],
    ["I'm having trouble with the website", ["If you're experiencing technical issues with the website, try clearing your browser cache. If the problem persists, contact our support team for further assistance."]],
    ["Tell me about your environmentally friendly initiatives", ["We are committed to sustainability and have various initiatives, such as using eco-friendly materials and reducing our carbon footprint. Visit our website for more details."]],
    ["Do you offer international shipping?", ["Yes, we offer international shipping. The shipping cost and delivery time vary by location. Check our 'Shipping' page for more information."]],
    ["How can I join your affiliate program?", ["To join our affiliate program, visit the 'Affiliates' section on our website and follow the registration process. Start earning commissions for promoting our products!"]],
    ["I want to change my email address", ["To update your email address, log in to your account and navigate to the 'Account Settings' page. Update your email, and the changes will take effect immediately."]],
    ["Tell me about your product reviews", ["We encourage customers to leave product reviews on our website. Your feedback helps other customers make informed decisions about our products. Thank you for sharing your experiences!"]],
    ["What safety measures do you have in place for in-store shopping?", ["In our physical stores, we have implemented safety measures such as social distancing, sanitization, and mask requirements to ensure a secure shopping environment."]],
    ["(.*)", ["I'm sorry, I didn't understand that. How may I assist you?"]]
]

def customer_support_chatbot():
    print("Welcome to Customer Support Chatbot. Type 'goodbye' to exit.")

    chat = Chat(pairs, reflections)

    while True:
        user_input = input("You: ").lower()

        if user_input == "goodbye":
            print(chat.respond(user_input))
            break

        response = chat.respond(user_input)
        print("Bot:", response)

if __name__ == "__main__":
    customer_support_chatbot()