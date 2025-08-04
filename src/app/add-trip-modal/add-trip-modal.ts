// src/app/add-trip-modal/add-trip-modal.component.ts
import { Component, EventEmitter, Output, Input } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms'; // <-- Import FormsModule
import { Trip } from '../models/trip.model';

@Component({
  selector: 'app-add-trip-modal',
  standalone: true,
  imports: [CommonModule, FormsModule], // <-- Add FormsModule here
  templateUrl: './add-trip-modal.component.html',
  styleUrls: ['./add-trip-modal.component.css']
})
export class AddTripModalComponent {
  // Input to control the visibility of the modal from the parent component
  @Input() isVisible: boolean = false;

  // Output events to communicate with the parent component
  @Output() close = new EventEmitter<void>();
  @Output() save = new EventEmitter<Omit<Trip, 'id'>>();

  // The model for our form, pre-filled with default values
  newTrip: Omit<Trip, 'id'> = {
    name: '',
    destination: '',
    start_date: '',
    end_date: '',
    budget: 0
  };

  // Method to handle form submission
  onSave(): void {
    // Basic validation
    if (this.newTrip.name && this.newTrip.destination) {
      this.save.emit(this.newTrip);
      this.resetForm();
    } else {
      alert('Please fill out at least the trip name and destination.');
    }
  }

  // Method to close the modal
  onClose(): void {
    this.close.emit();
    this.resetForm();
  }

  // Resets the form to its initial state
  private resetForm(): void {
    this.newTrip = {
      name: '',
      destination: '',
      start_date: '',
      end_date: '',
      budget: 0
    };
  }
}
