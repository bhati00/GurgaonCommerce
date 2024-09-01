export interface LoginResponse {
    access: string;
    refresh: string;
  }

export interface User{
    id: number,
    email : string,
    password : string,
    first_name : string,
    last_name : string,
    is_active : boolean
}

export interface UserProfile{
    
}