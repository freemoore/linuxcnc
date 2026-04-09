/* Modbus definition file for a 4-channel relay board found on eBay */

/*
The format of the channel descriptors is:

{TYPE, FUNC, ADDR, COUNT, pin_name}

TYPE is one of HAL_BIT, HAL_FLOAT, HAL_S32, HAL_U32
FUNC = 1, 2, 3, 4, 5, 6, 15, 16 - Modbus commands
COUNT = number of coils/registers to read
*/

#define MAX_MSG_LEN 40   // may be increased if necessary to max 251

static const hm2_modbus_chan_descriptor_t channels[] = {
/*  {TYPE,    FUNC, ADDR,   COUNT, pin_name} */
    {HAL_BIT, 1,  0x0000, 8,     "state"},
    {HAL_BIT, 2,  0x0000, 16,     "input"},
    {HAL_BIT, 5,  0x0004, 1,     "mbout-0.000"},
    {HAL_BIT, 5,  0x0004, 1,     "mbout-0.001"},
    {HAL_BIT, 5,  0x0004, 1,     "mbout-0.002"},
    {HAL_BIT, 5,  0x0004, 1,     "mbout-0.003"},
    {HAL_BIT, 5,  0x0004, 1,     "mbout-0.004"},
    {HAL_BIT, 5,  0x0005, 1,     "mbout-0.005"},
    {HAL_BIT, 5,  0x0006, 1,     "mbout-0.006"},
    {HAL_BIT, 5,  0x0007, 1,     "mbout-0.007"},
    {HAL_BIT, 5,  0x0008, 1,     "mbout-0.008"},
    {HAL_BIT, 5,  0x0009, 1,     "mbout-0.009"},
    {HAL_BIT, 5,  0x000a, 1,     "mbout-0.010"},
    {HAL_BIT, 5,  0x000b, 1,     "mbout-0.011"},
    {HAL_BIT, 5,  0x000c, 1,     "mbout-0.012"},
    {HAL_BIT, 5,  0x000d, 1,     "mbout-0.013"},
    {HAL_BIT, 5,  0x000e, 1,     "mbout-0.014"},
    {HAL_BIT, 5,  0x000f, 1,     "mbout-0.015"},

};


/* Optionally #define DEBUG to aid with troubleshooting.
   Use 3 to see a lot of information about the modbus
   internal workings. 1 is default (errors only)                    */

// vim: syn=c
