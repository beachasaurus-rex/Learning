using LearningWPF.Enums;

namespace LearningWPF.Models
{
    public class Motor : ProtoModel
    {
        #region Fields

        private MotorStatus _status;
        private int _id;
        private string _motorName;
        private RotationalDirection _direction;

        #endregion //Fields

        #region Properties

        public MotorStatus Status
        {
            get { return _status; }

            //This set method will determine if the input value is the
            //same as the current value -> if they are not the same, then
            //it will change the current value to the input value and
            //then it will notify the event handler that its value
            //has been changed.
            set
            {
                if (value != _status)
                {
                    _status = value;
                    OnPropertyChanged("Status");
                }
            }
        }
        public int ID
        {
            get { return _id; }
            set
            {
                if (value != _id)
                {
                    _id = value;
                    OnPropertyChanged("ID");
                }
            }
        }
        public string MotorName
        {
            get { return _motorName; }
            set
            {
                if (value != _motorName)
                {
                    _motorName = value;
                    OnPropertyChanged("MotorName");
                }
            }
        }
        public RotationalDirection Direction
        {
            get { return _direction; }
            set
            {
                if (value != _direction)
                {
                    _direction = value;
                    OnPropertyChanged("Direction");
                }
            }
        }

        #endregion //Properties

        #region Constructors

        public Motor(int id)
        {
            _status = MotorStatus.On;
            _id = id;
            _motorName = string.Format($"TestMotor{id}");
            _direction = RotationalDirection.CounterClockwise;
        }

        #endregion Constructors
    }
}
