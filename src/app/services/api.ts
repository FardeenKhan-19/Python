// src/app/services/api.ts

import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

// Define interfaces for type safety
export interface Hotel {
  name: string;
  price: string;
  location: string;
  image_url: string;
}

export interface Activity {
  place: string;
  cost: string;
}

export interface ItineraryDay {
  day: number;
  date: string;
  activities: Activity[];
}

export interface TripSummary {
    hotelCost: string;
    activityCost: string;
    totalCost: string;
}

export interface ImageRecognitionResponse {
    location: string;
    history: string;
}


@Injectable({
  providedIn: 'root'
})
export class ApiService {
  private baseUrl = 'http://127.0.0.1:5000/api'; // Your Flask backend URL

  constructor(private http: HttpClient) { }
    // Add these methods inside the ApiService class

  // Fetches the list of all available currency codes
  getCurrencies(): Observable<any> {
    return this.http.get('https://api.frankfurter.app/currencies');
  }

  // Fetches the latest exchange rate for a specific currency
  getExchangeRate(from: string, to: string): Observable<any> {
    return this.http.get(`https://api.frankfurter.app/latest?from=${from}&to=${to}`);
  }

  getHotels(): Observable<Hotel[]> {
    return this.http.get<Hotel[]>(`${this.baseUrl}/hotels`);
  }

  getItinerary(): Observable<ItineraryDay[]> {
    return this.http.get<ItineraryDay[]>(`${this.baseUrl}/itinerary`);
  }

  getSummary(): Observable<TripSummary> {
    // Note: The backend uses POST for this, even though it doesn't take a body.
    return this.http.post<TripSummary>(`${this.baseUrl}/summary`, {});
  }

  uploadImage(file: File): Observable<ImageRecognitionResponse> {
    const formData = new FormData();
    formData.append('image', file, file.name);
    return this.http.post<ImageRecognitionResponse>(`${this.baseUrl}/image-recognition`, formData);
  }
}