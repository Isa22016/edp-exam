class Event:
    def __init__(self, name, payload):
        self.name = name
        self.payload = payload

class ApplicationRejectedEvent(Event):
    def __init__(self, payload, job):
        super().__init__("embassy_reject_request", {"payload": payload, "job": job})

class ApplicationSubmittedEvent(Event):
    def __init__(self, payload, is_sumbit):
        super().__init__("submit_confirmation", {"payload": payload, "is_confirmed": is_sumbit})

communication_queue = []

class Company:
    def __init__(self, payload):
       
        self.payload = payload

    def ask_for_embassy(self, job):
        event = ApplicationRejectedEvent (self.payload, job)
        event = ApplicationSubmittedEvent (self.payload, job)
        communication_queue.append(event)
        print('Event', event.name, 'emitted!')
 
    def handle_appointment_request(self, event):
        print(f"Job {event.payload['job']} on {event.payload['company']}")
        confirmation_event = AppointmentConfirmationEvent(event.payload["job"], is_confirmed=True)
        communication_queue.append(confirmation_event)
        print('Event', confirmation_event.name, 'emitted!')
        
# Example Usage
Iskhak = Student("Iskhak1", "Facebook")
Maksud = Student("Maksud2", "AMD" )
Muhammad = Student("Muhammad3", "Goggle",)

Iskhak1.ApplicationRejectedEvent('10.12.2024')
Maksud2.AppointmentConfirmationEvent('11.12.2024')
Muhammad3.AppointmentConfirmationEvent('10.12.2024')



   

    
  