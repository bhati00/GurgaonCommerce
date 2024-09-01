import { LoginResponse, User } from "../common/types";
import axiosInstance from "../lib/axios";

export const login = async (userData: Partial<User>): Promise<LoginResponse> => {
  try {
    const response = await axiosInstance.post<LoginResponse>('/jwt/create', userData);
    const { access, refresh } = response.data;

    localStorage.setItem('accessToken', access);
    localStorage.setItem('refreshToken', refresh);
    return response.data;
  } catch (error) {
    console.error('Error Loggin user:', error);
    throw error;
  }
}

export const getUser = async (): Promise<User> => {
  try {
    const response = await axiosInstance.get<User>('/users/me/');
    return response.data;
  } catch (error) {
    console.error('Error fetching user:', error);
    throw error;
  }
};

