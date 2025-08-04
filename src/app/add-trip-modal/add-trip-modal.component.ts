// src/app/add-trip-modal/add-trip-modal.component.ts
import { Component, EventEmitter, Output, Input } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
// FIXED: The path must go up one directory to find the 'models' folder.
import { Trip } from '../models/trip.model'; 

@Component({
  selector: 'app-add-trip-modal',
  standalone: true,
  imports: [CommonModule, FormsModule],
  templateUrl: './add-trip-modal.component.html',
  styleUrls: ['./add-trip-modal.component.css']
})
export class AddTripModalComponent {
  @Input() isVisible: boolean = false;
  @Output() close = new EventEmitter<void>();
  // FIXED: This explicit type definition prevents the "index signature" error.
  @Output() save = new EventEmitter<{ name: string; destination: string; start_date: string; end_date: string; budget: number; }>();

  newTrip = {
    name: '',
    destination: '',
    start_date: '',
    end_date: '',
    budget: 0
  };

  onSave(): void {
    if (this.newTrip.name && this.newTrip.destination) {
      this.save.emit(this.newTrip);
      this.resetForm();
    } else {
      alert('Please fill out at least the trip name and destination.');
    }
  }

  onClose(): void {
    this.close.emit();
    this.resetForm();
  }

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
