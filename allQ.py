import tkinter as tk
from tkinter import messagebox
from collections import deque

class LinearQueue:
    def __init__(self, capacity):
        self.capacity = max(1, int(capacity))
        self.buffer = [None] * self.capacity
        self.front = 0
        self.rear = -1
        self.size = 0

    def is_full(self):
        return self.rear == self.capacity - 1

    def is_empty(self):
        return self.size == 0

    def enqueue(self, item):
        if self.is_full():
            return False
        self.rear += 1
        self.buffer[self.rear] = item
        self.size += 1
        return True

    def dequeue(self):
        if self.is_empty():
            return None
        item = self.buffer[self.front]
        self.buffer[self.front] = None
        self.front += 1
        self.size -= 1
        
        # Reset queue when empty to allow new entries
        if self.size == 0:
            self.front = 0
            self.rear = -1
            
        return item

    def to_list(self):
        items = []
        for i in range(self.front, self.rear + 1):
            if self.buffer[i] is not None:
                items.append(self.buffer[i])
        return items

class CircularQueue:
    def __init__(self, capacity):
        self.capacity = max(1, int(capacity))
        self.buffer = [None] * self.capacity
        self.head = 0
        self.tail = 0
        self.size = 0

    def is_full(self):
        return self.size == self.capacity

    def is_empty(self):
        return self.size == 0

    def enqueue(self, item):
        if self.is_full():
            return False
        self.buffer[self.tail] = item
        self.tail = (self.tail + 1) % self.capacity
        self.size += 1
        return True

    def dequeue(self):
        if self.is_empty():
            return None
        item = self.buffer[self.head]
        self.buffer[self.head] = None
        self.head = (self.head + 1) % self.capacity
        self.size -= 1
        return item

    def to_list(self):
        items = []
        idx = self.head
        for _ in range(self.size):
            items.append(self.buffer[idx])
            idx = (idx + 1) % self.capacity
        return items


class CustomDeque:
    def __init__(self, capacity):
        self.capacity = max(1, int(capacity))
        self.buffer = [None] * self.capacity
        self.front = 0
        self.rear = 0
        self.size = 0

    def is_full(self):
        return self.size == self.capacity

    def is_empty(self):
        return self.size == 0

    def insert_front(self, item):
        """Insert item at the front of the deque"""
        if self.is_full():
            return False
        self.front = (self.front - 1) % self.capacity
        self.buffer[self.front] = item
        self.size += 1
        return True

    def insert_rear(self, item):
        """Insert item at the rear of the deque"""
        if self.is_full():
            return False
        self.buffer[self.rear] = item
        self.rear = (self.rear + 1) % self.capacity
        self.size += 1
        return True

    def delete_front(self):
        """Delete item from the front of the deque"""
        if self.is_empty():
            return None
        item = self.buffer[self.front]
        self.buffer[self.front] = None
        self.front = (self.front + 1) % self.capacity
        self.size -= 1
        return item

    def delete_rear(self):
        """Delete item from the rear of the deque"""
        if self.is_empty():
            return None
        self.rear = (self.rear - 1) % self.capacity
        item = self.buffer[self.rear]
        self.buffer[self.rear] = None
        self.size -= 1
        return item

    def rotate_clockwise(self, steps=1):
        """Rotate deque clockwise by specified steps"""
        if self.is_empty():
            return
        steps = steps % self.size
        if steps == 0:
            return
        
        # Move front pointer forward
        self.front = (self.front + steps) % self.capacity
        self.rear = (self.rear + steps) % self.capacity

    def rotate_anticlockwise(self, steps=1):
        """Rotate deque anticlockwise by specified steps"""
        if self.is_empty():
            return
        steps = steps % self.size
        if steps == 0:
            return
        
        # Move front pointer backward
        self.front = (self.front - steps) % self.capacity
        self.rear = (self.rear - steps) % self.capacity

    def to_list(self):
        """Convert deque contents to list for display"""
        items = []
        idx = self.front
        for _ in range(self.size):
            items.append(self.buffer[idx])
            idx = (idx + 1) % self.capacity
        return items

    def get_front_item(self):
        """Get front item without removing it"""
        if self.is_empty():
            return None
        return self.buffer[self.front]

    def get_rear_item(self):
        """Get rear item without removing it"""
        if self.is_empty():
            return None
        rear_idx = (self.rear - 1) % self.capacity
        return self.buffer[rear_idx]


class TicketBookingSystem:
    def __init__(self, total_tickets, mode="standard", circular_capacity=10, deque_capacity=8):
        self.tickets = total_tickets
        self.mode = mode  # "standard" | "priority" | "circular" | "deque"
        self.linear_queue = LinearQueue(5)  # Fixed size of 5 for standard mode
        self.queue = deque()  # For priority mode
        self.vip_queue = deque()
        self.circular_queue = CircularQueue(circular_capacity)
        self.custom_deque = CustomDeque(deque_capacity)

    def set_mode(self, mode, circular_capacity=None, deque_capacity=None):
        self.mode = mode
        if mode == "circular" and circular_capacity is not None:
            self.circular_queue = CircularQueue(circular_capacity)
        elif mode == "deque" and deque_capacity is not None:
            self.custom_deque = CustomDeque(deque_capacity)

    def join_queue(self, customer_name, is_vip=False):
        if not customer_name:
            return "Name cannot be empty."

        if self.mode == "priority":
            if is_vip:
                self.vip_queue.append(customer_name)
                return f"{customer_name} (VIP) has joined the queue."
            else:
                self.queue.append(customer_name)
                return f"{customer_name} has joined the queue."

        if self.mode == "circular":
            ok = self.circular_queue.enqueue(customer_name)
            if ok:
                return f"{customer_name} has joined the circular queue."
            return "Queue is full. Cannot join right now."

        # standard
        ok = self.linear_queue.enqueue(customer_name)
        if ok:
            return f"{customer_name} has joined the queue."
        return "Queue is full. Cannot join right now."

    def join_deque_front(self, customer_name):
        """Join deque at front position"""
        if not customer_name:
            return "Name cannot be empty."
        ok = self.custom_deque.insert_front(customer_name)
        if ok:
            return f"{customer_name} has joined the deque at front."
        return "Deque is full. Cannot join right now."

    def join_deque_rear(self, customer_name):
        """Join deque at rear position"""
        if not customer_name:
            return "Name cannot be empty."
        ok = self.custom_deque.insert_rear(customer_name)
        if ok:
            return f"{customer_name} has joined the deque at rear."
        return "Deque is full. Cannot join right now."

    def serve_customer(self):
        # Determine emptiness based on mode
        if self.mode == "priority":
            no_customers = (not self.vip_queue) and (not self.queue)
        elif self.mode == "circular":
            no_customers = self.circular_queue.is_empty()
        elif self.mode == "deque":
            no_customers = self.custom_deque.is_empty()
        else:
            no_customers = self.linear_queue.is_empty()

        if no_customers:
            return "No customers in the queue."

        if self.tickets <= 0:
            return "Tickets are sold out."

        if self.mode == "priority":
            customer = self.vip_queue.popleft() if self.vip_queue else self.queue.popleft()
        elif self.mode == "circular":
            customer = self.circular_queue.dequeue()
        elif self.mode == "deque":
            customer = self.custom_deque.delete_front()  # Serve from front by default
        else:
            customer = self.linear_queue.dequeue()

        self.tickets -= 1
        return f"{customer} bought a ticket ✅ | Tickets left: {self.tickets}"

    def serve_deque_front(self):
        """Serve customer from front of deque"""
        if self.custom_deque.is_empty():
            return "No customers in the deque."
        if self.tickets <= 0:
            return "Tickets are sold out."
        
        customer = self.custom_deque.delete_front()
        self.tickets -= 1
        return f"{customer} bought a ticket from front ✅ | Tickets left: {self.tickets}"

    def serve_deque_rear(self):
        """Serve customer from rear of deque"""
        if self.custom_deque.is_empty():
            return "No customers in the deque."
        if self.tickets <= 0:
            return "Tickets are sold out."
        
        customer = self.custom_deque.delete_rear()
        self.tickets -= 1
        return f"{customer} bought a ticket from rear ✅ | Tickets left: {self.tickets}"

    def rotate_deque_clockwise(self, steps=1):
        """Rotate deque clockwise"""
        if self.custom_deque.is_empty():
            return "Deque is empty. Cannot rotate."
        self.custom_deque.rotate_clockwise(steps)
        return f"Deque rotated clockwise by {steps} step(s)."

    def rotate_deque_anticlockwise(self, steps=1):
        """Rotate deque anticlockwise"""
        if self.custom_deque.is_empty():
            return "Deque is empty. Cannot rotate."
        self.custom_deque.rotate_anticlockwise(steps)
        return f"Deque rotated anticlockwise by {steps} step(s)."

    def get_queue(self):
        if self.mode == "priority":
            # Show VIP first, then normal
            return [f"[VIP] {n}" for n in list(self.vip_queue)] + list(self.queue)
        if self.mode == "circular":
            return self.circular_queue.to_list()
        if self.mode == "deque":
            return self.custom_deque.to_list()
        return self.linear_queue.to_list()

    def clear_all_queues(self):
        """Clear all queues when switching modes"""
        # Clear linear queue
        self.linear_queue = LinearQueue(5)
        
        # Clear priority queues
        self.queue.clear()
        self.vip_queue.clear()
        
        # Clear circular queue
        self.circular_queue = CircularQueue(self.circular_queue.capacity)
        
        # Clear custom deque
        self.custom_deque = CustomDeque(self.custom_deque.capacity)
        
        # Reset tickets to original count (10)
        self.tickets = 10


class TicketBookingApp:
    def __init__(self, root):
        self.system = TicketBookingSystem(total_tickets=10)

        root.title("🎟️ Ticket Booking System")
        root.geometry("600x650")
        root.resizable(False, False)

        self.title_label = tk.Label(root, text="Ticket Booking System", font=("Arial", 16, "bold"))
        self.title_label.pack(pady=10)

        # Tickets remaining
        self.tickets_label = tk.Label(root, text=f"Tickets Left: {self.system.tickets}", font=("Arial", 12))
        self.tickets_label.pack(pady=5)

        # Mode selection
        mode_frame = tk.LabelFrame(root, text="Mode", padx=10, pady=5)
        mode_frame.pack(pady=5, fill="x", padx=10)
        self.mode_var = tk.StringVar(value="standard")
        self.rb_standard = tk.Radiobutton(mode_frame, text="Standard", variable=self.mode_var, value="standard", command=self.on_mode_change)
        self.rb_priority = tk.Radiobutton(mode_frame, text="Priority (VIP)", variable=self.mode_var, value="priority", command=self.on_mode_change)
        self.rb_circular = tk.Radiobutton(mode_frame, text="Circular", variable=self.mode_var, value="circular", command=self.on_mode_change)
        self.rb_deque = tk.Radiobutton(mode_frame, text="Deque (Double-ended)", variable=self.mode_var, value="deque", command=self.on_mode_change)
        self.rb_standard.pack(anchor="w")
        self.rb_priority.pack(anchor="w")
        self.rb_circular.pack(anchor="w")
        self.rb_deque.pack(anchor="w")

        # Capacity controls for circular and deque modes
        cap_frame = tk.Frame(root)
        cap_frame.pack(pady=2, fill="x", padx=10)
        
        # Circular capacity
        tk.Label(cap_frame, text="Circular Capacity:").pack(side="left")
        self.capacity_var = tk.IntVar(value=3)
        self.capacity_spin = tk.Spinbox(cap_frame, from_=1, to=1000, textvariable=self.capacity_var, width=6, state="disabled", command=self.on_capacity_change)
        self.capacity_spin.pack(side="left", padx=6)
        
        # Deque capacity
        tk.Label(cap_frame, text="Deque Capacity:").pack(side="left", padx=(20, 0))
        self.deque_capacity_var = tk.IntVar(value=8)
        self.deque_capacity_spin = tk.Spinbox(cap_frame, from_=1, to=1000, textvariable=self.deque_capacity_var, width=6, state="disabled", command=self.on_deque_capacity_change)
        self.deque_capacity_spin.pack(side="left", padx=6)

        # Name input and mode-specific controls
        input_frame = tk.Frame(root)
        input_frame.pack(pady=5)
        self.name_entry = tk.Entry(input_frame, width=20, font=("Arial", 12))
        self.name_entry.pack(side="left", padx=5)
        
        # VIP checkbox for priority mode
        self.vip_var = tk.BooleanVar(value=False)
        self.vip_check = tk.Checkbutton(input_frame, text="VIP", variable=self.vip_var, state="disabled")
        self.vip_check.pack(side="left", padx=5)
        
        # Position selection for deque mode
        self.position_var = tk.StringVar(value="rear")
        self.position_menu = tk.OptionMenu(input_frame, self.position_var, "front", "rear")
        self.position_menu.config(state="disabled")
        self.position_menu.pack(side="left", padx=5)

        # Actions
        btn_frame = tk.Frame(root)
        btn_frame.pack(pady=5)
        self.join_btn = tk.Button(btn_frame, text="Join Queue", command=self.join_queue, width=12, bg="lightblue")
        self.join_btn.pack(side="left", padx=2)
        self.serve_btn = tk.Button(btn_frame, text="Serve Customer", command=self.serve_customer, width=12, bg="lightgreen")
        self.serve_btn.pack(side="left", padx=2)
        
        # Deque-specific buttons
        self.serve_front_btn = tk.Button(btn_frame, text="Serve Front", command=self.serve_deque_front, width=12, bg="lightcoral", state="disabled")
        self.serve_front_btn.pack(side="left", padx=2)
        self.serve_rear_btn = tk.Button(btn_frame, text="Serve Rear", command=self.serve_deque_rear, width=12, bg="lightpink", state="disabled")
        self.serve_rear_btn.pack(side="left", padx=2)
        
        # Rotation buttons
        rot_frame = tk.Frame(root)
        rot_frame.pack(pady=2)
        self.rot_cw_btn = tk.Button(rot_frame, text="Rotate Clockwise", command=self.rotate_clockwise, width=15, bg="lightyellow", state="disabled")
        self.rot_cw_btn.pack(side="left", padx=2)
        self.rot_acw_btn = tk.Button(rot_frame, text="Rotate Anti-CW", command=self.rotate_anticlockwise, width=15, bg="lightcyan", state="disabled")
        self.rot_acw_btn.pack(side="left", padx=2)

        # Queue display
        self.queue_label = tk.Label(root, text="Current Queue:", font=("Arial", 12))
        self.queue_label.pack(pady=5)
        self.queue_listbox = tk.Listbox(root, width=50, height=12)
        self.queue_listbox.pack(pady=5)

        self.update_ui()

    def clear_all_queues(self):
        """Clear all queues in the system"""
        self.system.clear_all_queues()

    def on_mode_change(self):
        mode = self.mode_var.get()
        self.clear_all_queues()
        
        # Toggle UI elements depending on mode
        if mode == "priority":
            self.vip_check.config(state="normal")
            self.capacity_spin.config(state="disabled")
            self.deque_capacity_spin.config(state="disabled")
            self.position_menu.config(state="disabled")
            self.serve_front_btn.config(state="disabled")
            self.serve_rear_btn.config(state="disabled")
            self.rot_cw_btn.config(state="disabled")
            self.rot_acw_btn.config(state="disabled")
        elif mode == "circular":
            self.vip_check.config(state="disabled")
            self.capacity_spin.config(state="normal")
            self.deque_capacity_spin.config(state="disabled")
            self.position_menu.config(state="disabled")
            self.serve_front_btn.config(state="disabled")
            self.serve_rear_btn.config(state="disabled")
            self.rot_cw_btn.config(state="disabled")
            self.rot_acw_btn.config(state="disabled")
        elif mode == "deque":
            self.vip_check.config(state="disabled")
            self.capacity_spin.config(state="disabled")
            self.deque_capacity_spin.config(state="normal")
            self.position_menu.config(state="normal")
            self.serve_front_btn.config(state="normal")
            self.serve_rear_btn.config(state="normal")
            self.rot_cw_btn.config(state="normal")
            self.rot_acw_btn.config(state="normal")
        else:  # standard
            self.vip_check.config(state="disabled")
            self.capacity_spin.config(state="disabled")
            self.deque_capacity_spin.config(state="disabled")
            self.position_menu.config(state="disabled")
            self.serve_front_btn.config(state="disabled")
            self.serve_rear_btn.config(state="disabled")
            self.rot_cw_btn.config(state="disabled")
            self.rot_acw_btn.config(state="disabled")

        if mode == "circular":
            self.system.set_mode(mode, circular_capacity=self.capacity_var.get())
        elif mode == "deque":
            self.system.set_mode(mode, deque_capacity=self.deque_capacity_var.get())
        else:
            self.system.set_mode(mode)
        self.update_ui()

    def on_capacity_change(self):
        if self.mode_var.get() == "circular":
            self.system.set_mode("circular", circular_capacity=self.capacity_var.get())
            self.update_ui()

    def on_deque_capacity_change(self):
        if self.mode_var.get() == "deque":
            self.system.set_mode("deque", deque_capacity=self.deque_capacity_var.get())
            self.update_ui()

    def join_queue(self):
        name = self.name_entry.get().strip()
        mode = self.mode_var.get()
        
        if mode == "deque":
            position = self.position_var.get()
            if position == "front":
                msg = self.system.join_deque_front(name)
            else:  # rear
                msg = self.system.join_deque_rear(name)
        else:
            is_vip = self.vip_var.get() if mode == "priority" else False
            msg = self.system.join_queue(name, is_vip=is_vip)
        
        self.name_entry.delete(0, tk.END)
        self.update_ui()
        messagebox.showinfo("Info", msg)

    def serve_customer(self):
        msg = self.system.serve_customer()
        self.update_ui()
        messagebox.showinfo("Info", msg)

    def serve_deque_front(self):
        msg = self.system.serve_deque_front()
        self.update_ui()
        messagebox.showinfo("Info", msg)

    def serve_deque_rear(self):
        msg = self.system.serve_deque_rear()
        self.update_ui()
        messagebox.showinfo("Info", msg)

    def rotate_clockwise(self):
        msg = self.system.rotate_deque_clockwise()
        self.update_ui()
        messagebox.showinfo("Info", msg)

    def rotate_anticlockwise(self):
        msg = self.system.rotate_deque_anticlockwise()
        self.update_ui()
        messagebox.showinfo("Info", msg)

    def update_ui(self):
        self.tickets_label.config(text=f"Tickets Left: {self.system.tickets}")

        self.queue_listbox.delete(0, tk.END)
        for customer in self.system.get_queue():
            self.queue_listbox.insert(tk.END, customer)

if __name__ == "__main__":
    root = tk.Tk()
    app = TicketBookingApp(root)
    root.mainloop()
