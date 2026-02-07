// User type based on data-model.md
export interface User {
  id: string;
  email: string;
  name?: string;
  createdAt: string; // ISO date string
  updatedAt: string; // ISO date string
}

// Todo type based on data-model.md
export interface Todo {
  id: string;  // Changed from number to string to match UUID
  title: string;
  description?: string;
  status: string;  // Changed from completed: boolean to status: string
  createdAt: string; // ISO date string
  updatedAt: string; // ISO date string
  userId: string;
}

// AuthSession type based on data-model.md
export interface AuthSession {
  token: string;
  userId: string;
  expiresAt: string; // ISO date string
  createdAt: string; // ISO date string
}

// UIState type based on data-model.md
export interface UIState {
  currentView: 'signin' | 'signup' | 'dashboard';
  loading: boolean;
  error?: string;
  success?: string;
}

// API Response types
export interface ApiResponse<T = any> {
  success: boolean;
  data?: T;
  error?: string;
  message?: string;
}

// API Request types
export interface CreateTodoRequest {
  title: string;
  description?: string;
  status?: string;  // Changed from completed to status
}

export interface UpdateTodoRequest {
  title?: string;
  description?: string;
  status?: string;  // Changed from completed to status
}

export interface SignUpRequest {
  email: string;
  name: string;
  password: string;
}

export interface SignInRequest {
  email: string;
  password: string;
}

// Form validation types
export interface TodoFormValues {
  title: string;
  description?: string;
  status?: string;  // Added status field
}

export interface AuthFormValues {
  email: string;
  password: string;
}
