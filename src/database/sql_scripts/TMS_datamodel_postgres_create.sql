CREATE TABLE "public.Employee" (
	"employee_id" serial NOT NULL,
	"employee_email" TEXT NOT NULL,
	"employee_first_name" char NOT NULL,
	"employee_last_name" char NOT NULL,
	"employee_gender" char NOT NULL,
	"employee_date_of_birth" DATE NOT NULL,
	"employee_current_wt" int NOT NULL,
	"vemployee_view_rights" int NOT NULL,
	CONSTRAINT "Employee_pk" PRIMARY KEY ("employee_id")
) WITH (
  OIDS=FALSE
);



CREATE TABLE "public.CalendarEvent" (
	"wtr_id" serial NOT NULL,
	"employee_id" serial NOT NULL,
	"calendar_event_date_start" DATE NOT NULL,
	"calendar_event_date_end" DATE NOT NULL,
	"calendar_event_status" TEXT NOT NULL,
	"calendar_event_time_start" TIME NOT NULL,
	"calendar_event_time_end" TIME NOT NULL,
	"calendar_event_amount" bigint NOT NULL,
	"work_day_type" int NOT NULL,
	"calendar_event_comment" TEXT NOT NULL,
	CONSTRAINT "CalendarEvent_pk" PRIMARY KEY ("wtr_id")
) WITH (
  OIDS=FALSE
);



CREATE TABLE "public.work_day_typs" (
	"work_day_type_id" serial NOT NULL,
	"work_day_type_name" char NOT NULL,
	CONSTRAINT "work_day_typs_pk" PRIMARY KEY ("work_day_type_id")
) WITH (
  OIDS=FALSE
);



CREATE TABLE "public.Groupconnection" (
	"groupconnection_id" serial NOT NULL,
	"employee_id" bigint NOT NULL,
	"group_id" bigint NOT NULL,
	CONSTRAINT "Groupconnection_pk" PRIMARY KEY ("groupconnection_id")
) WITH (
  OIDS=FALSE
);



CREATE TABLE "public.Groups" (
	"group_id" serial NOT NULL,
	"group_title" char NOT NULL,
	CONSTRAINT "Groups_pk" PRIMARY KEY ("group_id")
) WITH (
  OIDS=FALSE
);



CREATE TABLE "public.Credential" (
	"email" TEXT NOT NULL,
	"password" TEXT NOT NULL,
	"employe_id" TEXT NOT NULL,
	CONSTRAINT "Credential_pk" PRIMARY KEY ("email")
) WITH (
  OIDS=FALSE
);




ALTER TABLE "CalendarEvent" ADD CONSTRAINT "CalendarEvent_fk0" FOREIGN KEY ("employee_id") REFERENCES "Employee"("employee_id");
ALTER TABLE "CalendarEvent" ADD CONSTRAINT "CalendarEvent_fk1" FOREIGN KEY ("work_day_type") REFERENCES "work_day_typs"("work_day_type_id");


ALTER TABLE "Groupconnection" ADD CONSTRAINT "Groupconnection_fk0" FOREIGN KEY ("employee_id") REFERENCES "Employee"("employee_id");
ALTER TABLE "Groupconnection" ADD CONSTRAINT "Groupconnection_fk1" FOREIGN KEY ("group_id") REFERENCES "Groups"("group_id");


ALTER TABLE "Credential" ADD CONSTRAINT "Credential_fk0" FOREIGN KEY ("employe_id") REFERENCES "Employee"("employee_id");







