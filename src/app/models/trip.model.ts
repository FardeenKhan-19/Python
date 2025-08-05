// src/app/models/trip.model.ts

export interface Trip {
  id: number;
  name: string;
  destinations: string;
  startDate: string;
  endDate: string;
  budget: number;
  spent: number;
  status: 'upcoming' | 'completed' | 'planning';
}