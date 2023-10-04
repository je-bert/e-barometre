export interface ErrorResponse {
  error: {
    message: string;
  };
  status: number;
  ok: boolean;
}

export interface SuccessResponse {
  body: {
    message: string;
  };
  status: number;
  ok: boolean;
}
